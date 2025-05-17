import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, movies_path, ratings_path, tags_path=None):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        self.tags_path = tags_path
        self._prepare_data()

    def _process_tags(self):
        tags = pd.read_csv(self.tags_path)
        movie_tags = tags.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()
        self.movies = self.movies.merge(movie_tags, on='movieId', how='left')
        self.movies['tag'] = self.movies['tag'].fillna('')

    def _prepare_data(self):
        self.movies['genres'] = self.movies['genres'].apply(lambda x: x.split('|'))
        
        if self.tags_path:
            self._process_tags()
        else:
            self.movies['tag'] = ''

        mlb = MultiLabelBinarizer()
        genre_matrix = pd.DataFrame(mlb.fit_transform(self.movies['genres']),
                                    columns=mlb.classes_, index=self.movies.index)

        self.movies = pd.concat([self.movies, genre_matrix], axis=1)

        # Vectorize tags
        from sklearn.feature_extraction.text import TfidfVectorizer
        tfidf = TfidfVectorizer(stop_words='english', max_features=200)
        tag_matrix = tfidf.fit_transform(self.movies['tag'])

        import scipy.sparse as sp
        genre_sparse = sp.csr_matrix(genre_matrix.values)
        self.features = sp.hstack([genre_sparse, tag_matrix])

        self.avg_ratings = self.ratings.groupby('movieId')['rating'].mean()

    def recommend(self, genre, min_rating=0.0, top_n=10):
        genre = genre.capitalize()
        if genre not in self.movies.columns:
            return pd.DataFrame()
        filtered = self.movies[self.movies[genre] == 1].copy()
        filtered['avg_rating'] = filtered['movieId'].map(self.avg_ratings)
        filtered = filtered[filtered['avg_rating'] >= min_rating]
        if filtered.empty:
            return pd.DataFrame()

        filtered_idx = filtered.index.tolist()
        filtered_features = self.features[filtered_idx]

        sim_matrix = cosine_similarity(filtered_features)
        filtered['sim_score'] = sim_matrix.mean(axis=1)
        recommendations = filtered.sort_values(['sim_score', 'avg_rating'], ascending=False)
        return recommendations[['title', 'avg_rating']].head(top_n)

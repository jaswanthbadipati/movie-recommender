import streamlit as st
from src.recommender import MovieRecommender

@st.cache(allow_output_mutation=True)
def load_recommender():
    return MovieRecommender('data/movies.csv', 'data/ratings.csv', 'data/tags.csv')

def main():
    st.title("🎬 Movie Recommendation System with Tags")
    st.write("Find movies by genre and rating, enhanced with user tags")

    recommender = load_recommender()
    genres = [col for col in recommender.movies.columns if col not in ['movieId', 'title', 'genres', 'tag']]

    genre = st.selectbox("Select Genre", sorted(genres))
    min_rating = st.slider("Minimum Rating", 0.0, 5.0, 3.0, 0.1)
    top_n = st.slider("Number of Recommendations", 5, 20, 10)

    if st.button("Recommend"):
        results = recommender.recommend(genre, min_rating, top_n)
        if results.empty:
            st.warning("No movies found with your criteria.")
        else:
            for _, row in results.iterrows():
                st.write(f"**{row['title']}** — Rating: {row['avg_rating']:.2f}")

if __name__ == '__main__':
    main()

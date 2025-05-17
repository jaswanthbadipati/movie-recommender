
# Movie Recommendation System with Tags

🎬 **Personalized movie recommendations** based on genre, user ratings, and enriched with user-generated tags, using content-based filtering and cosine similarity.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Datasets](#datasets)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [How It Works](#how-it-works)  
- [Technologies Used](#technologies-used)  
- [Future Improvements](#future-improvements)  
- [License](#license)  

---

## Overview

This project implements a content-based movie recommendation system that suggests movies to users by analyzing movie genres and user-generated tags. It leverages cosine similarity on combined feature vectors (genres + tags) and filters movies by user-selected genre and minimum average rating.

The system provides personalized, relevant movie suggestions and offers an intuitive web interface built with Streamlit.

---

## Features

- Filter movies by **genre** and **minimum average user rating**  
- Use **tags data** to enrich movie descriptions and improve recommendation quality  
- Compute **cosine similarity** between movie features for accurate similarity measurement  
- Interactive **Streamlit UI** for seamless user experience  
- Fast loading with **Streamlit caching** for data and model reuse  

---

## Datasets

This project uses the following datasets from [MovieLens](https://grouplens.org/datasets/movielens/) or [TMDb](https://www.themoviedb.org/documentation/api):

- `movies.csv` — Movie details including genres  
- `ratings.csv` — User ratings for movies  
- `tags.csv` — User-generated tags associated with movies (optional but recommended for better results)  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jaswanthbadipati/movie-recommendation-system.git
cd movie-recommendation-system
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser. Use the sidebar or widgets to:

- Select a movie **genre**  
- Set **minimum rating** filter  
- Choose the number of recommendations to display  

Click **Recommend** to get personalized movie suggestions.

---

## Project Structure

```
movie-recommendation-system/
│
├── data/
│   ├── movies.csv       # Movie metadata including genres
│   ├── ratings.csv      # User ratings for movies
│   └── tags.csv         # User-generated tags for movies
│
├── src/
│   └── recommender.py   # Core recommendation engine logic
│
├── app.py               # Streamlit app for user interface
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation (this file)
```

---

## How It Works

1. **Data Loading:** Loads movies, ratings, and tags datasets.  
2. **Preprocessing:**  
   - Splits genres into lists and converts them to a binary matrix.  
   - Aggregates tags per movie and vectorizes them with TF-IDF.  
   - Combines genres and tags into a single feature matrix.  
3. **Average Ratings:** Computes average ratings per movie for filtering.  
4. **Recommendation:**  
   - Filters movies by selected genre and minimum rating.  
   - Calculates cosine similarity between feature vectors.  
   - Scores and ranks movies by similarity and rating.  
   - Returns top N recommended movies.  
5. **User Interface:** Allows users to specify preferences and displays results interactively.

---

## Technologies Used

- Python 3.8+  
- Pandas — Data manipulation  
- Scikit-learn — TF-IDF vectorization, cosine similarity  
- Streamlit — Interactive web app framework  
- NumPy, SciPy — Scientific computing and sparse matrices  

---

## Future Improvements

- Add collaborative filtering to incorporate user-user or user-item similarities.  
- Integrate movie metadata like cast, director, or plot summaries for richer features.  
- Improve UI with poster images, summaries, and external links.  
- Deploy on cloud platforms for wider accessibility.  
- Add user login and personalized profiles for history-based recommendations.  

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

If you have questions, suggestions, or want to contribute, feel free to open an issue or submit a pull request!

---

**Enjoy your personalized movie journey! 🍿**

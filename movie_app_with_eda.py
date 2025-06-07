
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import ast
import pickle
import requests

st.set_page_config(layout="wide")

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Sidebar navigation
st.sidebar.title("🎬 Movie Recommender Dashboard")
page = st.sidebar.radio("Go to", ["Recommender System", "EDA & Visuals"])

# Function to fetch posters using TMDb API
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=aef1be404a0d300b91ad6532bafb7b56&language=en-US'
    response = requests.get(url)
    if response.status_code != 200:
        return "https://via.placeholder.com/500x750?text=No+Poster"
    data = response.json()
    poster_path = data.get('poster_path')
    if not poster_path:
        return "https://via.placeholder.com/500x750?text=No+Poster"
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Main content
if page == "Recommender System":
    st.title("🎬 Movie Recommender System")

    selected_movie_name = st.selectbox(
        'Select a movie to get recommendations:',
        movies['title'].values
    )

    if st.button("Recommend"):
        names, posters = recommend(selected_movie_name)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(names[0])
            st.image(posters[0])
        with col2:
            st.text(names[1])
            st.image(posters[1])
        with col3:
            st.text(names[2])
            st.image(posters[2])
        with col4:
            st.text(names[3])
            st.image(posters[3])
        with col5:
            st.text(names[4])
            st.image(posters[4])

elif page == "EDA & Visuals":
    st.title("📊 Movie Dataset EDA and Visualizations")

    # Reload raw TMDB CSVs
    movies_raw = pd.read_csv("tmdb_5000_movies.csv")
    credits_raw = pd.read_csv("tmdb_5000_credits.csv")
    movies_eda = movies_raw.merge(credits_raw, on='title')

    def extract_genres(genre_str):
        try:
            return [i['name'] for i in ast.literal_eval(genre_str)]
        except:
            return []

    all_genres = []
    for g in movies_eda['genres']:
        all_genres.extend(extract_genres(g))

    genre_counts = pd.Series(all_genres).value_counts()

    st.subheader("🎭 Top 10 Genres")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    genre_counts.head(10).plot(kind='bar', color='skyblue', ax=ax1)
    ax1.set_ylabel("Number of Movies")
    st.pyplot(fig1)

    def extract_cast(cast_str):
        try:
            return [i['name'] for i in ast.literal_eval(cast_str)[:3]]
        except:
            return []

    all_cast = []
    for c in movies_eda['cast']:
        all_cast.extend(extract_cast(c))

    cast_counts = pd.Series(all_cast).value_counts()

    st.subheader("👨‍🎤 Top 10 Frequent Actors")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    cast_counts.head(10).plot(kind='bar', color='orange', ax=ax2)
    ax2.set_ylabel("Number of Appearances")
    st.pyplot(fig2)

    st.subheader("📝 Word Cloud from Movie Overviews")
    overview_text = " ".join(movies_eda['overview'].dropna().values)
    wordcloud = WordCloud(width=1000, height=300, background_color='white').generate(overview_text)
    fig3, ax3 = plt.subplots(figsize=(10, 3))
    ax3.imshow(wordcloud, interpolation='bilinear')
    ax3.axis("off")
    st.pyplot(fig3)

    movies_eda['release_date'] = pd.to_datetime(movies_eda['release_date'], errors='coerce')
    movies_eda['year'] = movies_eda['release_date'].dt.year
    year_counts = movies_eda['year'].value_counts().sort_index()

    st.subheader("📅 Number of Movies Released Each Year")
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    ax4.plot(year_counts.index, year_counts.values, marker='o')
    ax4.set_xlabel("Year")
    ax4.set_ylabel("Number of Movies")
    st.pyplot(fig4)

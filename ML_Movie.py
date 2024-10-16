#Streamlit Application

import streamlit as st
import pickle
import pandas as pd

# Function to recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    for i in movies_list[1:7]:  # Skipping the first one as it is the same movie
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Display an image on the Streamlit app
st.image('moviepic.png', width=100)

# Title of the Streamlit app
st.title('Movie Recommendation System')

# Dropdown menu to select a movie
selected_movie_name = st.selectbox("Pick one please", movies['title'].values)

# Button to get recommendations
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
    st.write(selected_movie_name)

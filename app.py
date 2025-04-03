def classification():
    import pickle
    import pandas as pd
    import streamlit as st
    import requests

    def fetch_poster(movie_id):
        response = requests.get(
            'https://api.themoviedb.org/3/movie/{}?api_key=dd3172b48edb6d057dfad88a52f5e6c3&language=en-US'.format(
                movie_id))
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    def recommend(movie):
        index = movies[movies['title'] == movie].index[0]  #
        movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]  #
        recommended_movies = []
        recommended_movies_posters = []
        for m in movies_list:
            movie_id = movies.iloc[m[0]].id
            recommended_movies.append(movies.iloc[m[0]].title)  #
            recommended_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_posters

    movies_dict = movies_dict = pickle.load(open(r"C:\Users\drish\OneDrive\Desktop\CS\pythonAdvance\Projects\movieRecommenderSystem\movie_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)

    similarity = pickle.load(open(r"C:\Users\drish\OneDrive\Desktop\CS\pythonAdvance\Projects\movieRecommenderSystem\similarity.pkl", "rb"))

    st.title("Recommendation of Movie: ")
    selected_movie_name = st.selectbox("Select a movie from the dropdown", movies['title'].values)  #

    if st.button('Show Recommendation'):
        names, posters = recommend(selected_movie_name)

        cols = st.columns(5)  # Using st.columns() instead of beta_columns()
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])


classification()
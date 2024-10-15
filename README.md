
Movie Recommender System:

This is a movie recommender system that seeks to provide recommendations to users based on the similarity between the contents of the movies i.e by content based filtering.

The dataset that has been used: TMDB 5000 movie dataset 

Types of Recommender Systems:
1. Content Based:
   These recommend items similar to those a user liked in the past.
   They analyze item features like tags, genres, descriptions, etc.
   For example, if you liked action movies, it recommends other action movies.
   
3. Collaborative Filtering Based:
   These recommend items based on user behavior and preferences.
   They find patterns and similarities between users.
   For instance, if User A and User B have similar movie-watching habits, User A’s preferences can be used to recommend 
   movies to User B.


Vectorization involves calculating the similarity between movie tags by converting them into vectors. Each movie, identified by its ID, name, and tags, is represented as a vector in a 5000-dimensional space. This is achieved through a "Bag of Words" model where all tags are concatenated, and the 5000 most common words, based on frequency, are selected. These words are then compared with each movie's tags. Each movie thus becomes a vector of dimensions corresponding to these common words. Stop words are not considered in this process, ensuring more meaningful comparisons.

Streamlit has been used to develop an interactive and user-friendly movie recommendation system application. This framework enabled me to seamlessly transform my data scripts into a dynamic web app, allowing users to easily select movies and receive tailored recommendations

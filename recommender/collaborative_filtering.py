from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def get_user_item_matrix(data):
    return data.pivot(index='userId', columns='movieId', values='rating').fillna(0)

def user_similarity_recommendations(user_id, data, top_n=5):
    matrix = get_user_item_matrix(data)
    similarity = cosine_similarity(matrix)
    user_index = matrix.index.get_loc(user_id)
    sim_scores = list(enumerate(similarity[user_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]
    top_users = [matrix.index[i] for i, _ in sim_scores[:top_n]]
    return top_users

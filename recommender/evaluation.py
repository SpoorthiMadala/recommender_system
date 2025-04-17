from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
import matplotlib.pyplot as plt

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def mae(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)

def precision_at_k(predicted_ratings, k):
    precision_scores = []
    for user_ratings in predicted_ratings:
        recommended = user_ratings[:k]
        relevant = [r for r in recommended if r[1] >= 4.0]  # rating threshold
        precision_scores.append(len(relevant) / k)
    return np.mean(precision_scores)

def recall_at_k(predicted_ratings, actual_ratings, k):
    recall_scores = []
    for user_ratings, actual in zip(predicted_ratings, actual_ratings):
        recommended = set([r[0] for r in user_ratings[:k]])
        relevant = set(actual)
        recall_scores.append(len(recommended & relevant) / len(relevant) if relevant else 0)
    return np.mean(recall_scores)
def plot_precision_recall(ks, precisions, recalls):
    plt.plot(ks, precisions, label='Precision@K', marker='o')
    plt.plot(ks, recalls, label='Recall@K', marker='x')
    plt.xlabel('K')
    plt.ylabel('Score')
    plt.title('Precision & Recall vs K')
    plt.legend()
    plt.grid()
    plt.show()


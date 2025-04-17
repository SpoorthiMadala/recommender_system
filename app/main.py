from recommender.data_loader import load_data
from recommender.matrix_factorization import svd_train, predict_rating
from recommender.evaluation import rmse, mae, precision_at_k

def main():
    print("Loading data...")
    data = load_data()

    print("Training model using SVD...")
    model, predictions = svd_train(data)
    predicted = predict_rating(model, user_id=1, movie_id=50)
    print(f"Predicted rating for user 1 on movie 50: {predicted:.2f}")

    print("Done. You can now generate recommendations or evaluate.")
    

if __name__ == "__main__":
    main()

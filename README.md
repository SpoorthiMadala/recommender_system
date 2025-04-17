# recommender_system
This is a Movie Recommender System built using Collaborative Filtering and Matrix Factorization (SVD) techniques. The system predicts user ratings for movies and provides recommendations based on historical ratings data.

Features
SVD-based Recommendation: Matrix factorization using Singular Value Decomposition (SVD) to predict movie ratings.

Evaluation Metrics: RMSE (Root Mean Squared Error) for model evaluation.

Prediction: Predict ratings for unseen user-item pairs.

Data Loading: Read and preprocess data from CSV files containing user ratings and movie details.

Installation
Requirements
Python 3.7+

Required libraries (listed in requirements.txt)

1. Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/recommender-system.git
cd recommender-system
2. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
3. Add your data:
Ensure you have the following CSV files in the data/ directory:

ratings.csv: Contains user ratings for movies.

movies.csv: Contains movie details (ID, title, genre, etc.).

The ratings.csv file should have columns like:

csv
Copy
Edit
userId,movieId,rating
1,1,4.5
2,2,3.0
...
The movies.csv file should have columns like:

csv
Copy
Edit
movieId,title,genre
1,Toy Story,Animation
2,Jumanji,Adventure
...
Usage
1. Run the system:
bash
Copy
Edit
python app/main.py
This will load the data, train the model using SVD, and display the predicted rating for user 1 on movie 50.

2. Modify Prediction:
To predict ratings for different user-movie pairs, modify the user_id and movie_id in main.py:

python
Copy
Edit
predicted = predict_rating(model, user_id=1, movie_id=50)
3. Evaluation:
The model will output the RMSE (Root Mean Squared Error) after training, which evaluates the performance of the recommender.

python
Copy
Edit
RMSE: 0.9019
Code Structure
bash
Copy
Edit
recommender_system/
│
├── data/                         # Store raw and processed datasets
│   └── ratings.csv               # Ratings data
│   └── movies.csv                # Movie details data
│
├── recommender/                  # Core recommendation logic
│   ├── __init__.py
│   ├── data_loader.py            # Load and preprocess data
│   ├── collaborative_filtering.py # User-User / Item-Item based filtering
│   ├── matrix_factorization.py    # SVD-based recommendation
│   ├── evaluation.py             # RMSE, precision, recall metrics
│
├── app/                          # Application folder
│   └── main.py                   # Main script to run the recommender system
│
├── requirements.txt              # List of dependencies
└── README.md                     # This README file
Evaluation Metrics
RMSE (Root Mean Squared Error): Measures the average squared difference between predicted and actual ratings. A lower RMSE indicates better accuracy.

MAE (Mean Absolute Error): Measures the average absolute difference between predicted and actual ratings.

Contributing
Feel free to fork the project, make improvements, and submit pull requests. If you have ideas for additional features or improvements, open an issue.

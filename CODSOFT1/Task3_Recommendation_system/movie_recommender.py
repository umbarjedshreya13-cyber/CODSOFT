# --------------------------------------------
# SIMPLE MOVIE RECOMMENDATION SYSTEM
# Collaborative Filtering using SVD Algorithm
# --------------------------------------------

import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# --------------------------------------------
# Step 1: Load MovieLens Dataset
# --------------------------------------------

print("Loading dataset...")

url_data = "http://files.grouplens.org/datasets/movielens/ml-100k/u.data"
url_item = "http://files.grouplens.org/datasets/movielens/ml-100k/u.item"

ratings_columns = ["user_id", "item_id", "rating", "timestamp"]
df = pd.read_csv(url_data, sep="\t", names=ratings_columns)

movie_columns = [
    "item_id", "title", "release_date", "video_release_date", "IMDb_URL",
    "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy",
    "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror",
    "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"
]

movies = pd.read_csv(url_item, sep="|", names=movie_columns, encoding="latin-1")

print("Dataset Loaded Successfully!")

# --------------------------------------------
# Step 2: Prepare Data for Collaborative Filtering
# --------------------------------------------

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["user_id", "item_id", "rating"]], reader)

trainset, testset = train_test_split(data, test_size=0.2)

# --------------------------------------------
# Step 3: Train the Recommendation Model
# --------------------------------------------

print("\nTraining model using SVD algorithm...")
model = SVD()
model.fit(trainset)

# --------------------------------------------
# Step 4: Evaluate Model Accuracy
# --------------------------------------------

predictions = model.test(testset)

print("\nModel Evaluation:")
accuracy.rmse(predictions)

# --------------------------------------------
# Step 5: Recommendation Function
# --------------------------------------------

def recommend_movies(user_id, num_recommendations=5):
    print(f"\nGenerating recommendations for User {user_id}...")

    all_movie_ids = movies["item_id"].unique()
    rated_movies = df[df["user_id"] == user_id]["item_id"].values

    movies_to_predict = [mid for mid in all_movie_ids if mid not in rated_movies]

    predicted_ratings = []

    for movie_id in movies_to_predict:
        prediction = model.predict(user_id, movie_id)
        predicted_ratings.append((movie_id, prediction.est))

    predicted_ratings.sort(key=lambda x: x[1], reverse=True)

    top_movies = predicted_ratings[:num_recommendations]

    print(f"\nTop {num_recommendations} Recommended Movies:\n")

    for movie_id, rating in top_movies:
        title = movies[movies["item_id"] == movie_id]["title"].values[0]
        print(f"{title}  --> Predicted Rating: {rating:.2f}")

# --------------------------------------------
# Step 6: Run Example Recommendation
# --------------------------------------------

recommend_movies(user_id=1, num_recommendations=5)

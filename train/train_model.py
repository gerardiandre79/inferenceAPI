import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

texts = [
    "I love this product",
    "This is amazing",
    "Very good experience",
    "I hate this",
    "Terrible service",
    "Very bad"
]

labels = [1,1,1,0,0,0]

pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("model", LogisticRegression())
])

pipeline.fit(texts, labels)

joblib.dump(pipeline, "../model/sentiment_model.pkl")

print("model saved")
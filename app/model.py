import joblib

model = joblib.load("model/sentiment_model.pkl")

def predict(text):

    pred = model.predict([text])[0]

    if pred == 1:
        return "positive"

    return "negative"
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Simple training data
data = {
    "text": [
        "I love this product",
        "This is the worst experience",
        "Amazing service and quality",
        "Very bad and disappointing"
    ],
    "label": [1, 0, 1, 0]  # 1 = Positive, 0 = Negative
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

def predict_sentiment(text: str) -> str:
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return "Positive" if prediction == 1 else "Negative"

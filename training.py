import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib 


with open("intent_training_data.json", "r") as f:
    data = json.load(f)


df = pd.DataFrame(data)


X = df["text"]
y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=1000))
])


pipeline.fit(X_train, y_train)


y_pred = pipeline.predict(X_test)
print("🔍 Classification Report:\n", classification_report(y_test, y_pred))

joblib.dump(pipeline, "intent_classifier.joblib")
print("✅ Model saved as intent_classifier.joblib")

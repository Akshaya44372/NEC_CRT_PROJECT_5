import os
import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "data",
    "train.csv"
)

df = pd.read_csv(csv_path)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(df["text"], df["label"])

save_dir = os.path.join(
    BASE_DIR,
    "saved_models"
)

os.makedirs(save_dir, exist_ok=True)

save_path = os.path.join(
    save_dir,
    "classifier.pkl"
)

joblib.dump(model, save_path)

print("Model Saved Successfully")
print(save_path)
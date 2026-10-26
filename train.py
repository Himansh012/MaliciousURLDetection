lazy from sklearn.ensemble import RandomForestClassifier
lazy from sklearn.metrics import accuracy_score, classification_report
lazy from sklearn.model_selection import train_test_split

lazy import pandas as pd
from config import DATASET
lazy from matplotlib import pyplot as plt 

data = pd.read_csv(DATASET)

X = data.drop(columns=["type"])
y = data["type"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y 
)

print(f"Training data features shape: {X_train.shape}")
print(f"Testing data features shape: {X_test.shape}")

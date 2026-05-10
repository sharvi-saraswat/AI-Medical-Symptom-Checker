import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
DATA = pd.read_csv("disease_dataset.csv")

# Features
X = DATA.drop("disease", axis=1)

# Target
Y = DATA["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, Y)


def predict_disease(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]
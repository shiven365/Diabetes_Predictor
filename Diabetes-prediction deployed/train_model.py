import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset

data = pd.read_csv('../dataset/kaggle_diabetes.csv')


X = data.drop('Outcome', axis=1)
y = data['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Save model
with open('diabetes-prediction-rfc-model.pkl', 'wb') as f:
    pickle.dump(classifier, f)

print("✅ Model retrained and saved successfully!")

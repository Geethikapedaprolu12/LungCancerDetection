import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Example DataFrame (replace with your actual dataset)
data = {
    'GENDER': [1, 0, 1, 0],
    'AGE': [65, 70, 60, 55],
    'SMOKING': [1, 1, 0, 0],
    'YELLOW_FINGERS': [1, 0, 1, 0],
    'ANXIETY': [0, 1, 0, 1],
    'PEER_PRESSURE': [1, 1, 0, 0],
    'CHRONIC DISEASE': [1, 0, 1, 0],
    'FATIGUE': [1, 0, 1, 0],
    'ALLERGY': [0, 1, 0, 1],
    'WHEEZING': [1, 0, 1, 0],
    'ALCOHOL CONSUMING': [1, 0, 1, 0],
    'COUGHING': [1, 0, 1, 0],
    'SHORTNESS OF BREATH': [1, 0, 1, 0],
    'SWALLOWING DIFFICULTY': [1, 0, 1, 0],
    'CHEST PAIN': [1, 0, 1, 0],
    'LUNG_CANCER': [1, 0, 1, 0]  # Target variable
}

df = pd.DataFrame(data)

# Features and target
X = df.drop(columns=['LUNG_CANCER'])
y = df['LUNG_CANCER']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model/lung_cancer_model.pkl')

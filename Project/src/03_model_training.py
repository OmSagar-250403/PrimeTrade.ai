import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from pprint import pprint

# Load the data with features
df = pd.read_csv("features_data.csv")

# Encode the target variable
le = LabelEncoder()
df['Port_IDs_encoded'] = le.fit_transform(df['Port_IDs'].astype(str))

# Feature matrix and target vector
X = df.drop(columns=['Port_IDs', 'Port_IDs_encoded', 'Trade_History', 'features'])
y = df['Port_IDs_encoded']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize models
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=200, random_state=42),
    'Support Vector Classifier': SVC(kernel='linear', random_state=42)
}

results = {}

# Train and evaluate models
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = {'accuracy': accuracy}
    if hasattr(model, 'feature_importances_'):
        results[name]['feature_importances'] = model.feature_importances_

pprint(results)

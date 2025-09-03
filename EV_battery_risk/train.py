import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv('battery_data.csv')

# Define features (X) and target (y)
features = ['temperature', 'voltage', 'current', 'charge_cycles', 'health_score']
target = 'risk_level'

X = df[features]
y = df[target]

# Encode the categorical target variable
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model (optional)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model and the label encoder
joblib.dump(model, 'battery_risk_model.pkl')
joblib.dump(le, 'label_encoder.pkl')

print("Model and label encoder saved successfully.")
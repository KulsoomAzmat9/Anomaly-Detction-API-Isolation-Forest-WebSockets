import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# 1. Generate fake "normal" training data
# Most data between 40-60
np.random.seed(42)
X_train = np.random.normal(loc=50, scale=5, size=(1000, 1))

# 2. Scale the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 3. Train Isolation Forest
# contamination = how much % of data we expect to be anomalies
iso_forest = IsolationForest(contamination=0.05, random_state=42)
iso_forest.fit(X_train_scaled)

# 4. Save model and scaler
joblib.dump(iso_forest, 'iso_forest.pkl')
joblib.dump(scaler, 'scaler.pkl')

print("Model trained and saved as iso_forest.pkl")
print("Scaler saved as scaler.pkl")
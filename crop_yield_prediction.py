
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Sample dataset: you can replace this with real agricultural data
data = pd.DataFrame({
    'rainfall': [200, 300, 250, 400, 450, 500],
    'temperature': [25, 23, 27, 30, 29, 28],
    'soil_ph': [6.5, 6.8, 6.2, 7.0, 6.9, 6.7],
    'fertilizer_kg': [100, 120, 110, 130, 140, 150],
    'crop_yield': [2.5, 2.7, 2.6, 3.1, 3.2, 3.3]  # in tons/acre
})

# Features and target
X = data[['rainfall', 'temperature', 'soil_ph', 'fertilizer_kg']]
y = data['crop_yield']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a random forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("Predicted crop yields:", y_pred)
print("Mean Squared Error:", mse)


import numpy as np

# Sample input features: [rainfall (mm), temperature (°C), soil pH]
X = np.array([
    [200, 25, 6.5],
    [300, 23, 6.8],
    [250, 27, 6.2],
    [400, 30, 7.0],
    [450, 29, 6.9],
    [500, 28, 6.7],
    [320, 24, 6.4],
    [280, 26, 6.6]
])

# Output: crop yield (tons per hectare)
y = np.array([2.5, 2.7, 2.6, 3.1, 3.2, 3.3, 2.8, 2.9])

# Add bias (intercept) term
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # shape: (8, 4)

# Calculate weights using Normal Equation
theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Show weights
print("Model parameters:", theta)

# Predict crop yield for new field
# Example input: rainfall=310mm, temperature=26°C, soil_pH=6.5
new_input = np.array([[1, 310, 26, 6.5]])  # includes bias
predicted_yield = new_input.dot(theta)

print("Predicted crop yield:", round(predicted_yield[0], 2), "tons/hectare")


# Simulated predictions from an AI model
predicted_yield = 3.2  # in tons/hectare
recommended_fertilizer = 120  # in kg/hectare
recommended_irrigation = 4000  # in liters/hectare

# Thresholds for optimization
fertilizer_limit = 100  # optimal limit to reduce runoff
irrigation_limit = 3500  # optimal water use

# Optimization recommendations
def generate_recommendations(yield_prediction, fert, water):
    actions = []

    # Check fertilizer use
    if fert > fertilizer_limit:
        actions.append(f"- Reduce fertilizer to around {fertilizer_limit} kg/ha to avoid runoff.")
    else:
        actions.append("- Fertilizer usage is within eco-friendly limits.")

    # Check irrigation
    if water > irrigation_limit:
        actions.append(f"- Use drip irrigation or reduce water to {irrigation_limit} L/ha to conserve water.")
    else:
        actions.append("- Water usage is optimal.")

    # Boosting yield
    if yield_prediction < 3.0:
        actions.append("- Consider improving soil quality or adjusting planting schedule.")
    else:
        actions.append("- Expected yield is good. Maintain current practices.")

    return actions

# Get recommendations
recommendations = generate_recommendations(predicted_yield, recommended_fertilizer, recommended_irrigation)

# Print final action plan
print("Resource Optimization Plan:")
for rec in recommendations:
    print(rec)

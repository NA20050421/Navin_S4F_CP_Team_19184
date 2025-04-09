
# Simulated farm data across a region/country
num_farms = 1000  # Number of farms adopting AI

# Baseline (without AI)
baseline_yield = 2.5  # tons/hectare
baseline_fertilizer = 150  # kg/hectare
baseline_water = 5000  # liters/hectare

# With AI recommendations
ai_yield = 3.2  # tons/hectare (28% increase)
ai_fertilizer = 100  # kg/hectare (33% reduction)
ai_water = 3500  # liters/hectare (30% reduction)

# Total area per farm (hectares)
area_per_farm = 2

# Calculate total food production
total_yield_baseline = num_farms * area_per_farm * baseline_yield
total_yield_ai = num_farms * area_per_farm * ai_yield
extra_food = total_yield_ai - total_yield_baseline

# Resource savings
fertilizer_saved = num_farms * area_per_farm * (baseline_fertilizer - ai_fertilizer)
water_saved = num_farms * area_per_farm * (baseline_water - ai_water)

# Display results
print("=== AI & Global Food Security Simulation ===")
print(f"Farms using AI: {num_farms}")
print(f"Total food production increased by: {round(extra_food, 2)} tons")
print(f"Fertilizer saved: {fertilizer_saved} kg")
print(f"Water saved: {water_saved} liters")
print("This extra yield can feed thousands more people while reducing environmental impact.")

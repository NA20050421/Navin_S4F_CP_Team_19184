
# Simulate 500 small farms in a developing region
num_farms = 500

# Baseline (traditional methods)
baseline_yield = 2.0       # tons/hectare
baseline_fertilizer = 130  # kg/hectare
baseline_water = 4500      # liters/hectare
baseline_pesticide = 5     # liters/hectare

# With AI Recommendations (simulated)
ai_yield = 2.6             # tons/hectare (30% yield boost)
ai_fertilizer = 90         # kg/hectare (30% reduction)
ai_water = 3200            # liters/hectare (29% less water)
ai_pesticide = 3           # liters/hectare (40% reduction)

area_per_farm = 1.5  # hectares per small farm

# Calculations
def compute_impact(num_farms, area, base, ai, resource_name):
    saved = (base - ai) * num_farms * area
    print(f"{resource_name} saved: {saved} units")

# Display simulated results
print("=== AI & Sustainable Agriculture Impact Simulation ===")
print(f"Farms using AI: {num_farms}")
print(f"Yield increase: {(ai_yield - baseline_yield) * num_farms * area_per_farm:.2f} tons (boosted income + food supply)")
compute_impact(num_farms, area_per_farm, baseline_fertilizer, ai_fertilizer, "Fertilizer")
compute_impact(num_farms, area_per_farm, baseline_water, ai_water, "Water")
compute_impact(num_farms, area_per_farm, baseline_pesticide, ai_pesticide, "Pesticide")
print("Promotes environmental health, reduces input costs, and improves resilience.")

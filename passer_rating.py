def calculate_passer_rating(att, comp, yds, td, intc):
    # Step 1: Calculate the four intermediate components
    # Each component is scaled and clamped between 0 and 2.375
    
    a = ((comp / att) - 0.3) * 5
    b = ((yds / att) - 3) * 0.25
    c = (td / att) * 20
    d = 2.375 - ((intc / att) * 25)
    
    # Step 2: Apply the "Sovereign" Clamping (Clamping between 0 and 2.375)
    def clamp(value):
        return max(0, min(value, 2.375))
    
    a, b, c, d = map(clamp, [a, b, c, d])
    
    # Step 3: Final Calculation
    # Sum the components, divide by 6, and scale by 100
    rating = ((a + b + c + d) / 6) * 100
    
    return round(rating, 1)

# Test Data: Joe Montana 1984 Season
# 432 Attempts, 279 Completions, 3630 Yards, 28 TDs, 10 INTs
montana_rating = calculate_passer_rating(432, 279, 3630, 28, 10)

print(f"1984 Joe Montana Passer Rating: {montana_rating}")
# Expected output: 102.9
# Sovereign Autonomy Stress Test
liquidity = 5500
monthly_income = 1800
fixed_expenses = 2500

# The "Stress" Variables
unforeseen_buffer = 2000  # LLC back-taxes, moving costs, or tech gear
emergency_monthly_burn = 1500  # If expenses spike or income stops

# 1. Standard Scenario (The "Sovereign" Path)
net_monthly_flow = monthly_income - fixed_expenses
print("--- SOVEREIGN STATUS REPORT ---")
print(f"Current Monthly Savings: ${net_monthly_flow}")

# 2. Stress Test Scenario (The "Worst-Case" Path)
# We subtract the one-time buffer from liquidity first
conservative_liquidity = liquidity - unforeseen_buffer
worst_case_days = (conservative_liquidity / emergency_monthly_burn) * 30

print(f"\n--- STRESS TEST (Worst Case) ---")
print(f"One-time emergency buffer set aside: ${unforeseen_buffer}")
print(f"If expenses spike to ${emergency_monthly_burn}/mo...")
print(f"Your 'Hard Floor' runway is {worst_case_days:.0f} days.")
# The original simple calculation
print(f"Original Absolute Freedom: {(liquidity / fixed_expenses) * 30:.0f} days.")
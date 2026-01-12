# Sovereign Autonomy Tracker
liquidity = 13000
monthly_burn = 500  # Adjust to your current daily survival cost

months_of_freedom = liquidity / monthly_burn
days_of_freedom = months_of_freedom * 30

print("--- SOVEREIGN STATUS REPORT ---")
print(f"Total Liquidity: ${liquidity}")
print(f"Autonomy Runway: {months_of_freedom:.1f} months")
print(f"Total Days of Absolute Freedom: {days_of_freedom:.0f}")

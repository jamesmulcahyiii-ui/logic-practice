def calculate_kelly_bet(bankroll, odds, win_probability):
    # odds: Decimal odds (e.g., 2.0 for +100)
    # win_probability: Your estimated % chance of winning (0.0 to 1.0)
    
    b = odds - 1
    p = win_probability
    q = 1 - p
    
    # Kelly Formula: f* = (bp - q) / b
    fraction = (b * p - q) / b
    
    # We use "Quarter Kelly" (divide by 4) to be conservative
    safe_fraction = fraction / 4
    
    # Final bet amount in dollars
    bet_amount = bankroll * safe_fraction
    
    return max(0, round(bet_amount, 2))

# Your current Sovereign Variables
my_bankroll = 83.12
current_odds = 2.10 # Example: A slight underdog
estimated_win_prob = 0.60 # Your calculated 52% edge

suggested_bet = calculate_kelly_bet(my_bankroll, current_odds, estimated_win_prob)

print(f"Current Bankroll: ${my_bankroll}")
print(f"Optimal Sovereign Bet: ${suggested_bet}")
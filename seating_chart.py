def find_priority_costs(costs, target):
    # This dictionary remembers the costs we've already scanned
    seen = {}

    for index, amount in enumerate(costs):
        # Math: What is the 'partner' cost we need to find?
        needed = target - amount

        if needed in seen:
            # We found the pair! Return their positions.
            return [seen[needed], index]

        # Record this cost and its position
        seen[amount] = index

    return "No match found"

# Example: Your potential 2026 'spike' costs
# [Survival Burn, LLC Back-tax, Moving Costs, Tech Gear, Buffer]
cost_list = [500, 1600, 3000, 1500, 2000]
target_spike = 4500 # e.g., Moving (3000) + Tech Gear (1500)

result = find_priority_costs(cost_list, target_spike)
print(f"Target ${target_spike} found at positions: {result}")
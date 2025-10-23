'''
☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier
'''

def earn_points(price):
    """Calculate loyalty points earned for a single purchase."""
    whole_dollars = int(price)  # Get the whole dollar amount
    points = whole_dollars * 3   # Earn 3 points per whole dollar
    return points

def tier_label(points):
    """Determine the loyalty tier based on total points."""
    if points < 100:
        return "Bronze"
    elif 100 <= points < 500:
        return "Silver"
    else:
        return "Gold"

total_spent = 0.0
total_points = 0

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [3.75, 7.20, 15.00, 100.50, 250.00, 500.00]


for amount in purchases:
    total_spent += amount
    total_points += earn_points(amount)

final_tier = tier_label(total_points)


print("☕️ Loyalty Points Engine Challenge")
print(f"Total dollars spent: ${total_spent:.2f}")
print(f"Total points earned: {total_points}")
print(f"Final tier: {final_tier}")
# End-of-file (EOF)

# Input data
print("HEDGING SYSTEM WITH AUTOMATIC DISTRIBUTION")
print("=" * 112)

coef = [float(x) for x in input("Enter odds (1 X 2): ").split()]
bets = [float(x) for x in input("Enter bets (1 X 2): ").split()]

# Validation:
if len(coef) != 3 or len(bets) != 3:
    print("ERROR: You must enter exactly 3 odds and 3 bets!")
    exit()
    
total_income = sum(bets)

print(f"\nINPUT DATA:")
print(f"1: {bets[0]} at {coef[0]}")
print(f"X: {bets[1]} at {coef[1]}")
print(f"2: {bets[2]} at {coef[2]}")
print(f"Total income: {total_income}")
print("=" * 112)

# Hedging odds (2% discount)
hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]

# STEP 1: Find the riskiest outcome
payouts = [bets[i] * coef[i] for i in range(3)]
risks = [payout - total_income for payout in payouts]

most_risky_index = risks.index(max(risks))
most_risky_risk = risks[most_risky_index]
most_risky_payout = payouts[most_risky_index]

print(f"\nRISK ANALYSIS:")
for i in range(3):
    outcome = ["1", "X", "2"][i]
    status = "WARNING" if risks[i] > 0 else "SAFE"
    print(f"   {outcome}: {risks[i]:.0f} {status}")

# STEP 2: Hedge the riskiest outcome
if most_risky_risk > 0:
    hedge_risky_amount = most_risky_risk / (hedge_coefs[most_risky_index] - 1)
    print(f"\nHEDGE FOR RISKIEST OUTCOME ({['1', 'X', '2'][most_risky_index]}):")
    print(f"   Formula: {most_risky_risk:.0f} / ({hedge_coefs[most_risky_index]:.2f} - 1) = {hedge_risky_amount:.0f}")
else:
    hedge_risky_amount = 0
    print(f"\nNO RISK FOR HEDGING")

# STEP 3: Find the highest odds to guarantee 0 result
highest_coef_index = coef.index(max(coef))
highest_coef_payout = payouts[highest_coef_index]

print(f"\nGUARANTEE 0 FOR HIGHEST ODDS ({['1', 'X', '2'][highest_coef_index]} @ {coef[highest_coef_index]}):")
print(f"   Potential payout: {highest_coef_payout:.0f}")

# STEP 4: Calculate remaining cash
cash_after_hedge = total_income - hedge_risky_amount
excess_cash = cash_after_hedge - highest_coef_payout

print(f"\nCASH SITUATION:")
print(f"   Cash after hedge: {cash_after_hedge:.0f}")
print(f"   Excess for distribution: {excess_cash:.0f}")

# STEP 5: Distribute excess
hedge_amounts = [0, 0, 0]

if excess_cash > 0:
    other_outcomes = [i for i in range(3) if i != highest_coef_index]
    sum_other_hedge_coef = hedge_coefs[other_outcomes[0]] + hedge_coefs[other_outcomes[1]]
    base_amount = excess_cash / sum_other_hedge_coef

    print(f"\nEXCESS DISTRIBUTION:")
    print(f"   Sum of hedge odds: {hedge_coefs[other_outcomes[0]]:.2f} + {hedge_coefs[other_outcomes[1]]:.2f} = {sum_other_hedge_coef:.2f}")
    print(f"   Base value: {excess_cash:.0f} / {sum_other_hedge_coef:.2f} = {base_amount:.0f}")

    for i in other_outcomes:
        other_coef = hedge_coefs[[x for x in other_outcomes if x != i][0]]
        hedge_amounts[i] = other_coef * base_amount
        print(f"   {['1', 'X', '2'][i]}: {other_coef:.2f} × {base_amount:.0f} = {hedge_amounts[i]:.0f}")

# STEP 6: FINAL RESULTS
print(f"\nFINAL SIMULATION:")
print("=" * 112)

total_hedge = hedge_risky_amount + sum(hedge_amounts)
final_cash = total_income - total_hedge

for i in range(3):
    outcome = ["1", "X", "2"][i]
    payout = payouts[i]

    hedge_income = 0
    if i == most_risky_index:
        hedge_income += hedge_risky_amount * hedge_coefs[i]
    if hedge_amounts[i] > 0:
        hedge_income += hedge_amounts[i] * hedge_coefs[i]

    if i == highest_coef_index:
        result = 0  # Guaranteed 0 for highest odds
    else:
        result = final_cash + hedge_income - payout

    margin = (result / total_income) * 100

    print(f"SCENARIO {outcome}:")
    print(f"   CASH: {final_cash:.0f}")
    if hedge_income > 0:
        print(f"   HEDGE: +{hedge_income:.0f}")
    print(f"   PAYOUT: -{payout:.0f}")
    print(f"   RESULT: {result:.0f} ({margin:+.1f}% of total income)")
    print("-" * 40)

print(f"\nOVERALL STATISTICS:")
print(f"   Total income: {total_income:.0f}")
print(f"   Total hedge: {total_hedge:.0f}")
print(f"   Cash after all operations: {final_cash:.0f}")
print("=" * 112)

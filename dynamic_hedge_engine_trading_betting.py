# Входни данни
print("🎰 СИСТЕМА ЗА ХЕДЖИРАНЕ С АВТОМАТИЧНО РАЗПРЕДЕЛЯНЕ")
print("=" * 113)

coef = [float(x) for x in input("Въведете коефициенти (1 X 2): ").split()]
bets = [float(x) for x in input("Въведете залози (1 X 2): ").split()]

total_income = sum(bets)

print(f"\n📊 ВХОДНИ ДАННИ:")
print(f"1: {bets[0]}лв @ {coef[0]}")
print(f"X: {bets[1]}лв @ {coef[1]}")
print(f"2: {bets[2]}лв @ {coef[2]}")
print(f"Общ приход: {total_income}лв")
print("=" * 113)

# Хеджиращи коефициенти (2% дисконт)
hedge_coefs = [coef[0] * 0.98, coef[1] * 0.98, coef[2] * 0.98]

# СТЪПКА 1: Намиране на най-рисковия изход
payouts = [bets[i] * coef[i] for i in range(3)]
risks = [payout - total_income for payout in payouts]

most_risky_index = risks.index(max(risks))
most_risky_risk = risks[most_risky_index]
most_risky_payout = payouts[most_risky_index]

print(f"\n🔍 АНАЛИЗ НА РИСКА:")
for i in range(3):
    outcome = ["1", "X", "2"][i]
    status = "⚠️" if risks[i] > 0 else "✅"
    print(f"   {outcome}: {risks[i]:.0f}лв {status}")

# СТЪПКА 2: Хеджиране на най-рисковия изход
if most_risky_risk > 0:
    hedge_risky_amount = most_risky_risk / (hedge_coefs[most_risky_index] - 1)
    print(f"\n🛡️ ХЕДЖ НА НАЙ-РИСКОВИЯ ИЗХОД ({['1', 'X', '2'][most_risky_index]}):")
    print(f"   Формула: {most_risky_risk:.0f} / ({hedge_coefs[most_risky_index]:.2f} - 1) = {hedge_risky_amount:.0f}лв")
else:
    hedge_risky_amount = 0
    print(f"\n✅ НЯМА РИСК ЗА ХЕДЖИРАНЕ")

# СТЪПКА 3: Намиране на най-високия коефициент за гарантиране на 0 резултат
highest_coef_index = coef.index(max(coef))
highest_coef_payout = payouts[highest_coef_index]

print(f"\n🎯 ГАРАНТИРАНЕ НА 0 ЗА НАЙ-ВИСОКИЯ КОЕФ ({['1', 'X', '2'][highest_coef_index]} @ {coef[highest_coef_index]}):")
print(f"   Потенциално плащане: {highest_coef_payout:.0f}лв")

# СТЪПКА 4: Изчисляване на остатъка в касата
cash_after_hedge = total_income - hedge_risky_amount
excess_cash = cash_after_hedge - highest_coef_payout

print(f"\n💰 КАСОВА СИТУАЦИЯ:")
print(f"   Каса след хедж: {cash_after_hedge:.0f}лв")
print(f"   Излишък за разпределяне: {excess_cash:.0f}лв")

# СТЪПКА 5: Разпределяне на излишъка
hedge_amounts = [0, 0, 0]

if excess_cash > 0:
    other_outcomes = [i for i in range(3) if i != highest_coef_index]
    sum_other_hedge_coef = hedge_coefs[other_outcomes[0]] + hedge_coefs[other_outcomes[1]]
    base_amount = excess_cash / sum_other_hedge_coef

    print(f"\n🔄 РАЗПРЕДЕЛЯНЕ НА ИЗЛИШЪКА:")
    print(
        f"   Сума на хедж коефициентите: {hedge_coefs[other_outcomes[0]]:.2f} + {hedge_coefs[other_outcomes[1]]:.2f} = {sum_other_hedge_coef:.2f}")
    print(f"   Базова стойност: {excess_cash:.0f} / {sum_other_hedge_coef:.2f} = {base_amount:.0f}лв")

    for i in other_outcomes:
        other_coef = hedge_coefs[[x for x in other_outcomes if x != i][0]]
        hedge_amounts[i] = other_coef * base_amount
        print(f"   {['1', 'X', '2'][i]}: {other_coef:.2f} × {base_amount:.0f} = {hedge_amounts[i]:.0f}лв")

# СТЪПКА 6: ФИНАЛНИ РЕЗУЛТАТИ
print(f"\n🎲 ФИНАЛНА СИМУЛАЦИЯ:")
print("=" * 113)

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
        result = 0  # Гарантирано 0 за най-високия коефициент
    else:
        result = final_cash + hedge_income - payout

    margin = (result / total_income) * 100

    print(f"🔮 {outcome}:")
    print(f"   💰 Каса: {final_cash:.0f}лв")
    if hedge_income > 0:
        print(f"   📥 Хедж: +{hedge_income:.0f}лв")
    print(f"   📤 Плащане: -{payout:.0f}лв")
    print(f"   💵 РЕЗУЛТАТ: {result:.0f}лв ({margin:+.1f}% от общия приход)")
    print("-" * 40)

print(f"\n📈 ОБЩА СТАТИСТИКА:")
print(f"   Общ приход: {total_income:.0f}лв")
print(f"   Общ хедж: {total_hedge:.0f}лв")
print(f"   Каса след всички операции: {final_cash:.0f}лв")
print("=" * 113)

print("🎯 СИСТЕМАТА ПРИКЛЮЧИЛА!")


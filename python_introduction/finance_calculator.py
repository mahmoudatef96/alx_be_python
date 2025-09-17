monthely_income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expenses: "))
monthely_saving = monthely_income - expense
projected_savings = monthely_saving * 12 + (monthely_saving * 12 * 0.05)
print("Your monthly savings are $", monthely_saving)
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
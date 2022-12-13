# Define your savings goal as a percentage of your income
# Define your savings goal as a percentage of your income
savings_goal = 0.65

# Define your monthly expenses
housing = 1500
transportation = 400
food = 500
healthcare = 150
miscellaneous = 200
investment = 400
total_expenses = input("Enter your total expenses: ")


# Calculate your total monthly expenses
total_exponents = housing + transportation + food + healthcare + miscellaneous

# Initialize counters for total money earned, spent, invested, and saved
total_earned = 0
total_spent = 0
total_invested = 0
total_saved = 0

# Get the amount of your pay check
income = float(input("Enter the amount of your pay check: "))

# Get the total amount of your expenses
total_expenses = float(input("Enter the total amount of your expenses: "))

# Calculate how much you have left to save/invest each month
leftover = income - total_expenses

# Update counters based on current month's income and expenses
total_earned += income
total_spent += total_expenses


# Allocate money to different accounts
print("You have $" + str(leftover) + " left to allocate to your accounts.")
savings = float(input("Enter the amount to allocate to your savings account: "))
total_saved += savings
roth_ira = float(input("Enter the amount to allocate to your Roth IRA: "))
total_invested += roth_ira
acorns = float(input("Enter the amount to allocate to your Acorns account: "))
total_invested += acorns
random = float(input("Enter the amount to allocate to your other account: "))

# Print your budget
print("Income: $" + str(income))
print("Housing: $" + str(housing))
print("Transportation: $" + str(transportation))
print("Food and groceries: $" + str(food))
print("Healthcare: $" + str(healthcare))
print("Miscellaneous: $" + str(miscellaneous))
print("Savings: $" + str(savings))
print("Roth IRA: $" + str(roth_ira))
print("Acorns: $" + str(acorns))
print("Other account: $" + str(random))
print("Total earned: $" + str(total_earned))
print("Total spent: $" + str(total_spent))
print("Total invested: $" + str(total_invested))
print("Total saved: $" + str(total_saved))






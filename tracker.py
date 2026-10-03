# Installemnt 3

print("=" *40)
print("\t EXPENSE TRACKER")
print("   Simple, organized and easy to use!")
print("=" *40)

print("MAIN MENU")
print(" [1] Add an Expense \t\t (coming soon)")
print(" [2] View all expenses \t\t (coming soon)")
print(" [3] Show total spent \t\t (coming soon)")
print(" [4] Exit \t\t\t (coming soon)\n")

name = input("What is your name? ")
print (f"Welcome {name}! Let's log two expenses.\n")

subtotal = 0.0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your Budget? "))

print(f"\n{"-" *40}")

print("SUMMARY")
print(f"  - {item1}: \t\t ${amount1}")
print(f"  - {item2}: \t\t ${amount2}")

print(f"Subtotal: \t\t ${subtotal}")

average = subtotal / 2
print(f"Average: \t\t ${average}")

tax = subtotal * (float(tax_percent) / 100)
print(f"Tax ({float(tax_percent)}%): \t\t ${tax}")

total = subtotal + tax
print(f"Grand Total: \t\t ${total}")

over_budget = total > float(budget)
print(f"Overbudget? \t\t {over_budget}")

left = float(budget) - total
print(f"Left in the budget: \t ${left}")

print("-" *40)
print("Made by: Justin Louis A. Capuno  |  Installment 3")
print("=" *40)
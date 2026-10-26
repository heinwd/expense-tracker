# Installment 4

print("=" *40)
print("\t EXPENSE TRACKER")
print("   Know where your money goes.")
print("=" *40)

print("MAIN MENU")
print(" [1] Add an expense \t\t (coming soon)")
print(" [2] View all expenses \t\t (coming soon)")
print(" [3] Show total spent \t\t (coming soon)")
print(" [4] Exit \t\t\t (coming soon)\n")

name = input("What is your name? ")
print (f"Welcome, {name}! Let's log two expenses.\n")

subtotal = 0.0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

if (amount1 <= 50):
    print("Small expense.\n")
elif (amount1 > 50 and amount1 <= 100):
    print("Moderate expense.\n")
elif (amount1 > 100 and amount1 <= 200):
    print("Big expense.\n")
elif (amount1 > 200):
    print("Huge expense - are you sure?\n")
else:
    print("Cannot input negative or zero amounts.\n")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

if (amount2 <= 50):
    print("Small expense.\n")
elif (amount2 > 50 and amount2 <= 100):
    print("Moderate expense.\n")
elif (amount2 > 100 and amount2 <= 200):
    print("Big expense.\n")
elif (amount2 > 200):
    print("Huge expense - are you sure?\n")
else:
    print("Cannot input negative or zero amounts.\n")

if (amount1 > 100 and amount2 > 100):
    print("Two big expenses in a row - slow down!")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print("\n" + "-" *40)

print("SUMMARY")
print(f"  - {item1}: \t\t ${amount1}")
print(f"  - {item2}: \t\t ${amount2}")

print(f"Subtotal: \t\t ${subtotal}")

average = subtotal / 2
print(f"Average: \t\t ${average}")

tax = subtotal * (float(tax_percent) / 100)
print(f"Tax ({float(tax_percent)}%): \t\t ${tax}")

total = subtotal + tax
print(f"Grand total: \t\t ${total}")

over_budget = total > float(budget)
left = float(budget) - total
over_by = total - float(budget)

if (over_budget):
    print(f"Over budget by ${over_by}.")
elif (total > (.9) * float(budget)):
    print(f"Careful: only ${left} left.")
else:
    print(f"Within budget. ${left} left.")

print("-" *40)
print("Made by: Justin Louis A. Capuno  |  Installment 4")
print("=" *40)
# Installemnt 2

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

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

print("\n" + "-" *40)

print("SUMMARY")
print(f"  - {item1}: \t\t ${amount1}")
print(f"  - {item2}: \t\t ${amount2}")

total = amount1 + amount2
print(f"Total spent: \t\t ${total}")

average = total / 2
print(f"Average: \t\t ${average}")

print("-" *40)
print("Made by: Justin Louis A. Capuno  |  Installment 2")
print("=" *40)
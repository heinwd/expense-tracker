# Installment 5

print("=" *40)
print("\t EXPENSE TRACKER")
print("   Know where your money goes.")
print("=" *40)

name = input("\n What is your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print (f"Welcome, {name}!\n")

subtotal = 0.0
count = 0

while True:
    print("MAIN MENU")
    print(" [1] Add an expense")
    print(" [2] View all expenses \t\t (coming soon)")
    print(" [3] Show total spent")
    print(" [4] Exit\n")

    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        if amount <= 0:
            print("Cannot input negative or zero amounts.\n")
            continue
        subtotal += amount
        count += 1

        if amount <= 50:
            print("Small expense.\n")
        elif amount <= 100:
            print("Moderate expense.\n")
        elif amount <= 200:
            print("Big expense.\n")
        else:
            print("Huge expense - are you sure?\n")

    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.\n")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total

        print("SUMMARY")
        print(f"Expense: \t\t {count}")
        print(f"Subtotal: \t\t ${subtotal:.2f}")
        print(f"Tax ({tax_percent}%): \t\t ${tax:.2f}")
        print(f"Grand total: \t\t ${total:.2f}")

        over_budget = total > budget
        over_by = total - budget

        if over_budget:
            print(f"Over budget by ${over_by:.2f}!\n")
        elif total > 0.9 * budget:
            print(f"Careful: only ${left:.2f} left.\n")
        else:
            print(f"Within budget. ${left:.2f} left.\n")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        break

    else:
        print("Invalid choice. Please enter 1-4.\n")

print("-" *40)
print("Made by: Justin Louis A. Capuno  |  Installment 5")
print("=" *40)
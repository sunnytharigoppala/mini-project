# Expense Tracker

expenses = []
amounts = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Display Total Spending")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        expense = input("Enter expense name: ")
        amount = float(input("Enter expense amount: ₹"))

        expenses.append(expense)
        amounts.append(amount)

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\nExpense List:")
            for i in range(len(expenses)):
                print(f"{i+1}. {expenses[i]} - ₹{amounts[i]:.2f}")

    elif choice == "3":
        total = sum(amounts)
        print(f"\nTotal Spending: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
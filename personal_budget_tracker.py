def budget_transistion():
    transistion = []

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Budget")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            #Add income
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            transistion.append({"Income", amount, description})
            print("YAAY! You got money")

        elif choice == "2":
            #Add expense
            amount = float(input("Enter the amount: "))
            description = input("Enter the description: ")
            transistion.append({"Expense", amount, description})
            print("Sad you lost your money")

        elif choice == "3":
            total_income = sum(amount for type, amount, _ in transistion if type == 'Income')
            total_expenses = sum(amount for type, amount, _ in transistion if type == 'Expense')
            net_balance = total_income - total_expenses

            print("\n--- Summary ---")
            print(f"Total Income: ₹{total_income}")
            print(f"Total Expenses: ₹{total_expenses}")
            print(f"Net Balance: ₹{net_balance}")

            print("\n--- Transactions ---")
            for type, amount, description in transistion:
                print(f"{type}: ₹{amount} - {description}")
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
budget_transistion()
print("Welcome to Expense Tracker!")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")
    print("You selected:", choice)

    if choice == "1":
        print("You chose to add an expense.")
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        # Save to file
        with open("expenses.txt", "a") as file:
            file.write(f"{name},{amount}\n")

        print("Expense added successfully!")

    elif choice == "2":
        print("Your expenses:")

        try:
            with open("expenses.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("No expenses saved yet.")
                else:
                    total = 0
                    for line in lines:
                        name, amount = line.strip().split(",")
                        print(f"{name}: Rs. {amount}")
                        total += float(amount)

                    print(f"\nTotal Spent: Rs. {total}")
        except FileNotFoundError:
            print("No expenses file found yet.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")


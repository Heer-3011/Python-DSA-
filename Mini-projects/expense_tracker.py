# Add expense
# View expense
# Delete expense 

def add_expense():
    name = input("Enter name of the expense: ").strip()
    amount = int(input("Enter amount: "))

    expense[name] = amount
    print(f"Record added successfully: {name} -> {amount}") 

def view_expense(): 
    print(expense)
    for keys,values in expense:
        print(keys,"=",values)

def delete_expense():
    name = input("Enter name of expense you want to delete: ").strip()

    if name in expense:
        expense.pop(name)
        print("Expense deleted!!!!") 
    else:
        print("Expense not found!")


if __name__ == "__main__":
    global expense

    while True:
        print("\n\n\tWelcome to expense tracker\n\n")
        print("Select option\n\t1. Add expense\n\t2. View expense\n\t3. Delete expense\n\t4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expense()

        elif choice == 3:
            delete_expense()

        elif choice == 4:
            break

        else:
            print("Invalid choice")
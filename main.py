expenses = []
budget = 0
menu_choice = "0"
def add_expenses():
    try:
        added = float(input("Enter your Expense:"))
        if added <= 0 :
            print("please enter a number greater than Zero!!")
        else:
            category = input("Enter your category for Expense:")
            expense = {
             "amount" : added ,
             "category" : category
             }
            expenses.append(expense)
            print("Successfully Added Rs.", added, "for", category)
    except ValueError: 
        print("please add something valid!!")        
def view_expenses():
    if not expenses:
        print("Expenses not added yet")
    else:
        for val in expenses :
            print("amount =", val["amount"], "used for", val["category"])

def edit_expenses():
    try:
        if not expenses:
            print("Please add any expenses first.")
        else:
            edit = int(input("Enter which expense do you want to edit:"))

            if edit >= 1 and edit <= len(expenses):
                new_exp = float(input("Enter your new expense:"))

                if new_exp <= 0:
                    print("Please enter a number greater than zero!")
                else:
                    idx = edit - 1
                    expenses[idx]["amount"] = new_exp
                    print("Value updated successfully!")

            else:
                print("Expense number out of range!")

    except ValueError:
        print("Please enter a valid number!")

def delete_expenses():
    try:
        if not expenses:
            print("please Add any Expenses first.")
        else:
            delete = int(input("Enter which one you want to delete:"))
            idx = delete - 1
            if delete >= 1 and len(expenses) >= delete:
                expenses.pop(idx)
                print("your expense", delete, "is deleted")
            else:
                print("Expense Number out of range")
    except ValueError:
        print("Please enter a valid number!")
def set_budget():
    try:
        global budget
        new_budget = float(input("Set your Monthly Budget:"))

        if new_budget <= 0:
            print("Please enter a valid amount")
        else:
            budget = new_budget
            print("Your budget is:", budget)
    except ValueError:
        print("Please enter something valid!")

def view_summary():
    total = 0
    for val in expenses:
        total += val["amount"]
    print("your total expenses are:", total)
    if budget == 0 :
        print("please set your budget first")
    elif total < budget :
        remaining = budget - total
        print("your remaining budget is:", remaining)
    elif total == budget :
        print("you have used all your budget")
    else:
        print("Warning!! you are out of budget.")

while menu_choice != "7":  
    print("PERSONAL EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Set Monthly Budget")
    print("6. View Summary")
    print("7. Exit")

    menu_choice = input("Enter your Choice(1 - 7):")
    print("You Selected:", menu_choice)

    if menu_choice == "1":
        print("Add Expense Selected")
        add_expenses()
    elif menu_choice == "2":
        print("View Expense Selected")
        view_expenses()
    elif menu_choice == "3":
        print("Edit Expense Selected") 
        edit_expenses()    
    elif menu_choice == "4":
        print("Delete Expense Selected")
        delete_expenses()
    elif menu_choice == "5":
        print("Set Monthly Budget")
        set_budget()
    elif menu_choice == "6":
        print("View Summary Selected")
        view_summary()
    elif menu_choice == "7":
        print("Exit Selected")
    else:
        print("Invalid Choice. Please Select a valid option (1 - 7).")


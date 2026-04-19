categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment",
]
 
category_examples = [
    "Lunch, snacks, coffee",
    "Bus, jeepney, ride-share",
    "Load, data plan, WiFi top-up",
    "Notebook, pen, bond paper",
    "Games, movies, hangout",
]
 
digits = "0123456789"
 

valid = False
while not valid:
    student_name = input("Student name: ")
    if student_name == "":
        print("  [Invalid] This field cannot be empty. Please try again.")
    else:
        found_digit = False
        for letter in student_name:
            if letter in digits:
                found_digit = True
        if found_digit:
            print("  [Invalid] Name must not contain numbers. Please try again.")
        else:
            valid = True
 

valid = False
while not valid:
    budget_input = input("Weekly budget: ")
    dot_count = 0
    is_num = True
    if budget_input == "":
        is_num = False
    for letter in budget_input:
        if letter == ".":
            dot_count += 1
            if dot_count > 1:
                is_num = False
        elif letter not in digits:
            is_num = False
    if not is_num:
        print("  [Invalid] Please enter a valid number (e.g. 500 or 49.75).")
    else:
        weekly_budget = float(budget_input)
        if weekly_budget <= 0:
            print("  [Invalid] Amount must be greater than 0. Please try again.")
        else:
            valid = True
 

print()
print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
for i in range(len(categories)):
    print(f" {i + 1}. {categories[i]:<22} [e.g. {category_examples[i]}]")
print("==========================================")
 

expenses = []
total_spent = 0.0
high_expense_threshold = weekly_budget * 0.25
 
for entry_num in range(1, 5):
    print(f"\n--- EXPENSE {entry_num} ---")
 
   
    valid = False
    while not valid:
        cat_input = input("Category (0 to skip): ")
        is_int = True
        if cat_input == "":
            is_int = False
        for letter in cat_input:
            if letter not in digits:
                is_int = False
        if not is_int:
            print("  [Invalid] Category must be a whole number (0 to skip, 1-5 to select).")
        else:
            category_input = int(cat_input)
            if 0 <= category_input <= 5:
                valid = True
            else:
                print("  [Invalid] Please enter a number from 0 to 5.")
 
    if category_input != 0:
 
       
        valid = False
        while not valid:
            description = input("Description: ")
            if description == "":
                print("  [Invalid] Description cannot be empty. Please try again.")
            else:
                valid = True
 
        
        valid = False
        while not valid:
            amount_input = input("Amount: ")
            dot_count = 0
            is_num = True
            if amount_input == "":
                is_num = False
            for letter in amount_input:
                if letter == ".":
                    dot_count += 1
                    if dot_count > 1:
                        is_num = False
                elif letter not in digits:
                    is_num = False
            if not is_num:
                print("  [Invalid] Please enter a valid number (e.g. 65 or 49.75).")
            else:
                amount = float(amount_input)
                if amount <= 0:
                    print("  [Invalid] Amount must be greater than 0. Please try again.")
                else:
                    valid = True
 
        is_high = amount > high_expense_threshold
        category_name = categories[category_input - 1]
 
        expenses.append({
            "category": category_name,
            "description": description,
            "amount": amount,
            "high": is_high,
        })
 
        total_spent += amount
 

remaining = weekly_budget - total_spent
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."
 

print()
print("======================================================")
print(f"     {student_name.upper()} -- WEEKLY EXPENSE LOG")
print("======================================================")
print(f"  Weekly Budget  : P{weekly_budget:.2f}")
 
for i, expense in enumerate(expenses, start=1):
    high_tag = "  ! High Expense Alert!" if expense["high"] else ""
    print(f"  [{i}] {expense['category']}")
    print(f"      {expense['description']:<36} P{expense['amount']:.2f}{high_tag}")
 
print("------------------------------------------------------")
print(f"  Total Spent    : P{total_spent:.2f}")
print(f"  Remaining      : P{remaining:.2f}")
print(f"  Status         : {status}")
print("======================================================")

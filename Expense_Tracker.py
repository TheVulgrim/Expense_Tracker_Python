import csv
import os

expense_list = {
    "food": 0,
    "travel": 0,
    "personal": 0,
    "savings": 0
}

file_path = "expenses.csv"

if os.path.exists(file_path):
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                cat, amount = row[0], row[1]
                if cat in expense_list:
                    try:
                        expense_list[cat] += int(amount)
                    except ValueError:
                        pass

print("-------------Expense-Tracker---------------")

with open(file_path, 'a', newline="") as file:
    writer = csv.writer(file)
    
    while True:
        category = input("Which category it belong to, Food / Travel / Personal / Savings (exit to see total):").lower().strip()
        
        if category == "exit":
            break
            
        if category not in expense_list:
            print("invalid category")
            continue
            
        try:
            Expense = int(input("Enter the expense :"))
        except ValueError:
            print("invalid input! Please enter a number.")
            continue
        
        if Expense > 0:
            expense_list[category] += Expense
            writer.writerow([category, Expense])
        else:
            print("invalid expense amount")

    print(expense_list)

print("Your Total Expense Is : ", sum(expense_list.values()))
print("-------------Thank-You for using this Expense Tracker!!!!--------------")

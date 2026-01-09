import csv
expense_list = {"food" : 0 ,
        "travel" : 0,
        "personal" : 0,
        "savings": 0
        
        }
print("-------------Expense-Tracker---------------")
file_path = "expenses.csv"
with open(file_path,'a', newline="") as file:
    while True:
        category = input("Which category it belong to, Food / Travel / Personal / Savings (exit to see total):").lower().strip()
        if category == "exit":
            break
        Expense = int(input("Enter the expense :"))
        
        
        if Expense > 0 and category in expense_list:
            expense_list[category] += Expense
            
        else:
            print("invalid")
        writer = csv.writer(file)
        writer.writerow([category, Expense])
        

    print(expense_list)

print("Your Total Expense Is : ",sum(expense_list.values()))

print("-------------Thank-You for using this Expense Tracker!!!!--------------")

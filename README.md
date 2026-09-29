# Expense Tracker (Python CLI)

A simple command-line tool to track your daily expenses by category. Every entry is saved to a local CSV file, and your totals are loaded back the next time you run it, so nothing resets.

## Features

- **Category tracking**: Food, Travel, Personal, and Savings
- **Totals that persist**: previous entries are read from `expenses.csv` on startup, so your running totals carry over between runs
- **Input validation**: bad input never crashes the program or gets saved:
  - text instead of a number (`abc`)
  - decimals (`49.5`); amounts are whole numbers
  - zero or negative amounts
  - unknown categories (`banana`)
- **Simple summary**: shows the total for each category and the overall total when you type `exit`

## Requirements

- Python 3.6+
- No external packages (uses only the standard library: `csv`, `os`)

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/TheVulgrim/Expense_Tracker_Python.git
   cd Expense_Tracker_Python
   ```

2. Run the script:

   ```bash
   python Expense_Tracker.py
   ```

   On Linux or macOS you may need `python3` instead of `python`. The filename is case-sensitive: it's `Expense_Tracker.py`.

3. Type a category, then the amount. Repeat for each expense. Type `exit` to see your totals and quit.

## Example Session

```
-------------Expense-Tracker---------------
Which category it belong to, Food / Travel / Personal / Savings (exit to see total):food
Enter the expense :250
Which category it belong to, Food / Travel / Personal / Savings (exit to see total):food
Enter the expense :49.5
invalid input! Please enter a number.
Which category it belong to, Food / Travel / Personal / Savings (exit to see total):banana
invalid category
Which category it belong to, Food / Travel / Personal / Savings (exit to see total):travel
Enter the expense :-5
invalid expense amount
Which category it belong to, Food / Travel / Personal / Savings (exit to see total):travel
Enter the expense :40
Which category it belong to, Food / Travel / Personal / Savings (exit to see total):exit
{'food': 250, 'travel': 40, 'personal': 0, 'savings': 0}
Your Total Expense Is :  290
-------------Thank-You for using this Expense Tracker!!!!--------------
```

Run it again and add more expenses: the totals continue from where you left off.

## How Your Data Is Stored

Valid expenses are appended to `expenses.csv`, which is created in the folder you run the script from. Each line is `category,amount`:

```csv
food,250
travel,40
```

- On startup, the tracker reads this file and adds up each category, so totals carry over.
- Invalid entries are never written to the file.
- Rows with an unknown category or a non-numeric amount are skipped when loading.
- To reset everything, delete `expenses.csv`.

## Project Structure

```
Expense_Tracker_Python/
├── Expense_Tracker.py   # The program
├── expenses.csv         # Created on first run (your data)
└── README.md
```

## Known Limitations

- Amounts must be whole numbers (no decimals)
- Pressing `Ctrl+C` exits with a Python traceback instead of showing your totals

## Ideas for Future Improvements

- [ ] Support decimal amounts
- [ ] Add a date to each expense and show monthly summaries
- [ ] Custom categories
- [ ] Edit or delete past entries
- [ ] Unit tests with `pytest`
- [ ] A Flask + SQL web version

## Author

**Rishi**: [@TheVulgrim](https://github.com/TheVulgrim)

## License

Add a license (for example, [MIT](https://choosealicense.com/licenses/mit/)) before sharing widely.

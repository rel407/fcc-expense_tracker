# Add an expense to the list
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})  # Add a dictionary with amount and category to the list

# Print all expenses in the list
def print_expenses(expenses):
    for expense in expenses:
        # Print each expense with its amount and category
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Calculate the total expenses
def total_expenses(expenses):
    # Use sum and map to get the total amount of all expenses
    return sum(map(lambda expense: expense['amount'], expenses))

# Filter expenses by a specific category
def filter_expenses_by_category(expenses, category):
    # Use filter to return expenses that match the given category
    return filter(lambda expense: expense['category'] == category, expenses)

# Main function to run the Expense Tracker program
def main():
    expenses = []  # Initialize an empty list to store expenses
    while True:
        # Display menu options to the user
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')  # Get user input for menu choice

        if choice == '1':  # Add an expense
            amount = float(input('Enter amount: '))  # Get user input for expense amount
            category = input('Enter category: ')  # Get user input for expense category
            add_expense(expenses, amount, category)  # Call function to add the expense

        elif choice == '2':  # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)  # Call function to print all expenses

        elif choice == '3':  # Show total expenses
            print('\nTotal Expenses: ', total_expenses(expenses))  # Call function to calculate total expenses

        elif choice == '4':  # Filter expenses by category
            category = input('Enter category to filter: ')  # Get user's choice for category to filter
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)  # Call function to filter expenses
            print_expenses(expenses_from_category)  # Print filtered expenses

        elif choice == '5':  # Exit the program
            print('Exiting the program.')
            break  # Exit the loop and terminate the program

# Call the main function to run the program
main()

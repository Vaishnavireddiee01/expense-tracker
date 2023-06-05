#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt

expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def analyze_expenses():
    categories = list(expenses.keys())
    amounts = list(expenses.values())

    plt.bar(categories, amounts)
    plt.xlabel('Categories')
    plt.ylabel('Amount')
    plt.title('Expense Tracker')
    plt.show()

def main():
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Analyze Expenses")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            add_expense(category, amount)
            print("Expense added successfully!")

        elif choice == '2':
            if not expenses:
                print("No expenses to analyze.")
            else:
                analyze_expenses()

        elif choice == '3':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


# In[ ]:





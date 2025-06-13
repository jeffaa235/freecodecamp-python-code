# Budget App Project

In this budget app project, we implemented a budget tracking app by having a `Category` class to track our expenses using a `ledger` variable
in the class. First, a `Category(name)` instance is created. Deposits can be added with `category.deposit(amount)` and a description can be
attached optionally. Withdrawals can be entered with `category.withdraw(amount)` and a description can be
attached optionally and transfers between two categories can be done with `category.transfer(amount, targetCategory)`.

This project also utilized internal functions such as `_get_withdrawals_balance()` which is only called by `get_spending()`. For example,
`_get_withdrawals_balance()` returns a negative number while `get_spending()` returns a positive number for true spending in human terms.

By implementing the `__str__()` special function, calling `print()` on a `Category` instance will output the category in a list view.
Moreover, `create_spending_chart(categories)` outputs a convenient chart that compares the percentage spent by category given a list of
categories.

## Example input
```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
```

## Output
![image](https://github.com/jeffaa235/freecodecamp-python-code/blob/main/budget-app-project/budget-app-project.png?raw=true)

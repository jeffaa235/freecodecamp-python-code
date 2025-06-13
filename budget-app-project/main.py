class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        length_of_name = len(self.name)
        length_of_title = 30
        asterisks_left = (length_of_title - length_of_name) // 2
        asterisks_right = length_of_title - length_of_name - asterisks_left
        title = '*' * asterisks_left + self.name + '*' * asterisks_right

        def limit_string(input_string, n, prepend_spaces=False, append_spaces=False):
            if len(input_string) > n:
                return input_string[:n]
            else:
                spaces = n - len(input_string)
                if prepend_spaces:
                    return ' ' * spaces + input_string
                elif append_spaces:
                    return input_string + ' ' * spaces
                else:
                    return input_string

        lines = [title]
        for transaction in self.ledger:
            current_line = ''
            current_line += limit_string(
                transaction['description'], 23, 
                append_spaces=True
            )

            amount_str = f'{transaction["amount"]:.2f}'
            current_line += limit_string(
                amount_str, 7, 
                prepend_spaces=True
            )
            lines.append(current_line)

        lines.append(f'Total: {self.get_balance():.2f}')         

        return '\n'.join(lines)


    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount, 
            'description': description
        })
        return True

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -1 * amount, 
                'description': description
            })
            return True
        else:
            return False

    def get_balance(self):
        balance = sum([transaction['amount'] for transaction in self.ledger])
        return balance

    def transfer(self, amount, targetCategory):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {targetCategory.name}')
            
            targetCategory.deposit(amount, f'Transfer from {self.name}')

            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        else:
            return True

    def _get_withdrawals_balance(self):
        withdrawals = sum([transaction['amount'] for transaction in self.ledger if transaction['amount'] < 0])
        return withdrawals

    def get_spending(self):
        return -1 * self._get_withdrawals_balance()


def create_spend_chart(categories):
    spendings = {category.name: round(category.get_spending(), 2) for category in categories}
    total_spending = sum(spendings.values())
    percentages = {category: round(spendings[category] / total_spending * 100) for category in spendings}
    bar_heights = {category: percentages[category] // 10 for category in percentages}
        
    chart = ['Percentage spent by category']
    for line in range(10, -1, -1):
        percent = f'{line*10}|'.rjust(4, ' ')
        dots = "  ".join(['o' if line <= bar_heights[category] else ' ' for category in bar_heights])
        
        chart.append(f'{percent} {dots}  ')

    # Create bar
    bar_length = len(categories) * 3 + 1
    bar = 4 * ' ' + bar_length * '-'
    chart.append(bar)

    # Extract chart labels from categories
    chart_labels = [category.name for category in categories]
    # Determine the maximum label length
    max_height = max([len(label) for label in chart_labels])
    # Iterate over each character position in the labels
    for i in range(max_height):
        # Extract the character at the current position from each label
        chars = [label[i] if i < len(label) else ' ' for label in chart_labels]

        chart.append(' ' * 5 + '  '.join(chars) + '  ')

    return ('\n'.join(chart))



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(29, 'department store')
auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(50, 'car tax')

print(food)
print()
print(create_spend_chart([food, clothing, auto]))

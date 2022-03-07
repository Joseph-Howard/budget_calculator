class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list([])
        self.funds = 0.0

    def __repr__(self):
        Print_Header = self.name.center(30,'*')+"\n"
        Print_Ledger = ''
        Print_total = f'Total:{self.funds:.2f}'

        for item in self.ledger:
            Printed_Description = "{:<23}".format(item['description'])
            Printed_Amount = "{:>7.2f}".format(item['amount'])
            Print_Ledger += "{}{}\n".format(Printed_Description[:23], Printed_Amount[:7])

        return (Print_Header+Print_Ledger+Print_total)

    def deposit(self, amount, description=''):
        amount = abs(amount)
        self.ledger.append({"amount":amount,"description":description})
        self.funds += amount
        print(self.ledger)
        #print(self.ledger)

    def withdraw(self,amount, description = ''):
        amount = -abs(amount)
        if self.check_funds(amount) == True:
           self.ledger.append({"amount":amount,"description":description})
           self.funds += amount
        else:
           return False

    def transfer(self,amount,Second_Self):
        x = Category(Second_Self)
        if  self.withdraw(amount,f'Transfer to {x.name}'):
            x.deposit(amount,f'Transfer to {self.name}')
            return True
        else:
            return False

    def get_balance(self):
        return self.funds


    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    spent_amount = []
    # Get total spent in each category.
    for cat in categories:
        cat_spent = 0
        for line in cat.ledger:
            if line['amount'] < 0:
                cat_spent += abs(line["amount"])
        spent_amount.append(float("{:.2f}".format(cat_spent)))
    print(spent_amount)
    total=sum(spent_amount)
    spending_percentage=list(map(lambda i: float("{:.2f}".format(i/total*100)),spent_amount))
    print(spending_percentage)

    spending_chart =""
    header = "Percentage spent by category"

    for i in reversed(range(0,101,10)):
        spending_chart += str(i).rjust(3)+'|'
        for j in spending_percentage:
            if j >= i:
                spending_chart += " o "
            else:
                spending_chart += "   "
        spending_chart +=" \n"
    print(spending_chart)

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions_list = []
    for i in categories:
        descriptions_list.append(i.name)
        #print(descriptions_list)

    max = len(descriptions_list[0])
    for i in descriptions_list:
        if max < len(i):
            max = len(i)
    #print('max:',max)

    line = []
    for i in range(max):
        for j in descriptions_list:
            try:
                line.append(j[i])
            except:
                line.append(' ')
                continue

    #print(line,'\n')

    for i in line:
        footer += "   "+"".join(map(lambda j: j.center(3), i)) + " \n"

    return (header + spending_chart + footer).rstrip("\n")

    #descriptions = list(map(lambda category: category.name, categories))
    #max_length = max(map(lambda description: len(description), descriptions))
    #descriptions = list(map(lambda description: description.ljust(max_length), descriptions))



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))

customer = input("welcome to the bank of plug" 
                "\nClick 1 to withdraw money"
                "\n click 2 to add money to the account"
                "\n click 3 to quit\n")
if customer =="1":
    balance = int(input("your balance here"))
    withdraw = int(input("how much would you like to withdraw"))
    if balance < withdraw:
        print("account overdraft balance", (balance - withdraw))
    else:
        print("your new balance:", (balance - withdraw))

import csv

class client:
# File name = main.py
    def __init__(self, customer_id, title, first_name, last_name,
                 birth_date, gender, email, occupation, account_balance, overdraft_limit):
        self.customer_id = customer_id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.email = email
        self.occupation = occupation
        self.account_balance = account_balance
        self.overdraft_limit = overdraft_limit

def read(self):


    filename = "client_data.csv"
    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)


    for row in csvreader:
            rows.append(row)

    print(rows)








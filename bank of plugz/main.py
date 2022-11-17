import csv

#parent class
class client:
    def __init__(self, customer_id, first_name, last_name,
                 birth_date, gender,):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender


    def show_details(self):
        print("client details")
        print("id ",self.customer_id)
        print("name ",self.first_name + self.last_name)
        print("birth date ",self.birth_date)
        print("gender ",self.gender)
#child class
class bank:
    def __init__(self, customer_id, first_name, last_name,
                  birth_date, gender,):
        super().__init__(customer_id, first_name, last_name,
                         birth_date, gender,)
        self.balance = int()
        self.client = client
    def add_funds(self,amount):
        self.balance = self.balance + self.amount
        print("current account balance  : £", self.balance)
    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("you have entered your overdraft current balance is",
                  self.balance - self.amount)
        else:
            self.balance -= self.amount
            print("balance has been updated new balance is",
                  self.balance)
    def see_balance(self):
        self.show_details()
        print("current account balance  : £", self.balance)


class client_manager:
    def __init__(self):
        self.client = []

    def create_list(self):
        with open("clients.csv") as f:
            reader = csv.reader(f)
            for line in reader:
                #parts = line.strip().split(",")
                #self.client.append(client(parts[1],parts[2],parts[3],parts[4],parts[5]))
                self.client.append(line)



    def get_client(self):
        return self.client

    def clients_in_overdraft(self):
        self.create_list()
        final = []

        for i in range(1,len(self.client)):
            test = self.client[i][8]
            overdraft = -abs(int(self.client[i][9]))
            balance = int(test)
            if balance < overdraft :
                final.append(str(self.client[i][2]))
        print(final)
bank_user = client_manager()
bank_user.create_list()
bank_user.clients_in_overdraft()

# print("welcome")
# user_id = range(1, 100, 1,)
# id = int(input("please enter user id"))
# customer = input("welcome to the bank of plug"
#                    "\n to see details type show_details()"
#                    "\n to add funds type add_funds()"
#                    "\n to withdraw type withdraw()"
#                    "\n to see account balance type see_balance()\n")




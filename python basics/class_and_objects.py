class Car:
    def __init__(self):
        pass
    
    def set_details(self, name, year):
        self.name = name
        self.year = year
    def get_details(self):
        print("Car name is", self.name, "and year is", self.year)

class Bank:
    def __init__(self):
        self.__name = None
        self.__balance = 0

    def deposit(self, name, balance):
        self.__name = name
        self.__balance = max(0, balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawal amount ", amount, " successful. New balance:", self.__balance)

    def get_details(self):
        print("Bank name:", self.__name, "Balance:", self.__balance)



if __name__ == "__main__":
    bank = Bank()
    bank.deposit("Vishal", 1000)
    # print(bank.name) now they are private so we can't access them directly
    # print(bank.balance)
    bank.get_details()
    bank.withdraw(100)
    bank.get_details()
    
    
    
    
    # car1 = Car()
    # car2 = Car()
    # car3 = Car()
    # car1.set_details("BMW", 2019)
    # car2.set_details("Audi", 2018)
    # car3.set_details("Honda", 2017)
    # car1.get_details()
    # car2.get_details()
    # car3.get_details()
    
    
    
    
from datetime import datetime

# Remi P 
# I&C SCI_X426.64 (FALL 2019/REG 00204/SEC 1) 
# Week 5 Assignment 10.27.2019

#Problem 1
#Create a vehicle parent class that has the methods `drive` 
# and `stop`, and the properties `weight` and `horsepower`.  
# Then create three child classes: `Car`, `Motorcycle`, and 
# `Truck`. `Car` will have the property wheels, equal to 4.  
# `Motorcycle` will have the wheel property set to 2, and the 
# method `wheelie`. `Truck` will have the property wheels set 
# to 6, and will have the method 'dump'.
class Vehicle:
    '''Vehicle parent class'''
    def __init__(self, weight, horsepower):
        self.weight = weight
        self.horsepower = horsepower

    def drive(self):
        print("Driving...")

    def stop(self):
        print("Stoppping...")


class Car(Vehicle):
    '''Car child class of Vehicle'''
    def __init__(self, weight, horsepower):
        self.wheels = 4
        super().__init__(weight, horsepower)


class Motorcycle(Vehicle):
    '''Motorcycle child class of Vehicle'''
    def __init__(self, weight, horsepower):
        super().__init__(weight, horsepower)
        self.wheels = 2

    def wheelie(self):
        print("Doing a wheelie...")


class Truck(Vehicle):
    '''Truck child class of Vehicle'''
    def __init__(self, weight, horsepower):
        super().__init__(weight, horsepower)
        self.wheels = 6

    def dump(self):
        print("Doing a dump...")




#Problem 2
#Create a class called NumericList that behaves just like a 
# list except it has an additional method called `product` 
# that will calculate the product of the items in the list. 
class NumericList(list):
    '''NumericList extends list class and implements
    a product method to calculate the product of ites from list'''
    def product(self):
        listLen = len(self)
        prod = 1
        for item in range(listLen):
            val = self.__getitem__(item)
            prod = prod * val
        return prod




#Problem 3
#Copy the customer class from the customer.py file that is part 
# of this week's material. Add the method 'get_first_purchase' 
# which will return the value of the first purchase the customer 
# has made. Also add 'get_sum_of_purchases' which will return the
# sum of all the purchases the customer as made.
class Customer:
    '''
    A class to model customers

    Parameters
    ----------
    customer_number : int, str
        the numerical customer id

    customer_info_filepath : str
        the filepath to the customer info file

    purchases_filepath : str
        the filepath to the purchases file

    '''
    def __init__(self, customer_number, customer_info_filepath,
                 purchases_filepath):
        self.customer_number = str(customer_number)
        self.customer_info_filepath = customer_info_filepath
        self.purchases_filepath = purchases_filepath
        self.purchases = {}

    def _load_customer_info(self):
        '''Load the data from the customer info file for this customer'''
        with open(self.customer_info_filepath, 'r') as read_file:
            for line in read_file:
                line_splits = line.strip().split(',')
                if line_splits[0] == self.customer_number:
                    self.name = line_splits[1]
                    self.age = line_splits[2]
                    self.state = line_splits[3]
                    break

    def _load_purchases(self):
        '''Load the purchases data from the purchases file, for this customer
        '''
        with open(self.purchases_filepath, 'r') as read_file:
            for line in read_file:
                line_splits = line.strip().split(',')
                if line_splits[0] == self.customer_number:
                    purchase_date = datetime.strptime(line_splits[1],
                                                      "%Y-%m-%d %H:%M:%S")
                    self.purchases[purchase_date] = line_splits[2]

    def load_data(self):
        '''Load all the customers data'''
        self._load_customer_info()
        self._load_purchases()

    def get_last_purchase(self):
        '''return the most recent purchase made by the customer'''
        return self.purchases[max(self.purchases.keys())]

    def get_first_purchase(self):
        '''return the first purchase made by the customer'''
        return self.purchases[min(self.purchases.keys())]

    def get_sum_of_purchases(self):
        '''returns the sum of all the purchases the customer as made'''
        total = 0
        for key in self.purchases:
            total = total + float(self.purchases[key])
        return total

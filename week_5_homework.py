# Remi P 
# I&C SCI_X426.64 (FALL 2019/REG 00204/SEC 1) 
# Week 5 Assignment 10.27.2019
from functools import wraps
import logging

#Problem 1
#Write a decorator, called mylogging, that can be used to 
# add a logging entry to a log file everytime the decorated 
# function is called. The log entry should include the function
# name and the values of the arguments (both positional and 
# keyword) that are passed to the function.
def mylogging(func):
    '''create a function that executes func logs the name
    of func'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''log the name of func and then execute func.'''
        logging.debug("Debug Name - {0}, args - {1}, kwargs - {2}".format(func.__name__,args,kwargs))
        logging.warning("Warning Name - {0}, args - {1}, kwargs - {2}".format(func.__name__,args,kwargs))
        result = func(*args, **kwargs)
        return result
    return wrapper 






#Problem 2
#Create a class called Person. This class will define a person object with the following properties: 
# name, height, weight.  It will also have a property called bmi that will be dynamically 
# calculated via getter method (use the property decorator)
class Person:
    '''The formula for bmi is weight / height squared. 
    The weight needs to be weight in kilograms and height needs to be in meters.'''
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
       #self.BMI = 1

    @property
    def BMI(self):
        value = self.weight/(self.height*self.height)
        return value


#Problem 3
#Create a class called "LinearModel". This class will allow you to 
# create an object that can make predictions according to the model y=mx+b. 
class LinearModel:
    '''This class will allow you to create an object that can 
    make predictions according to the model y=mx+b'''
    def __init__(self, m, b):
        self.m = m
        self.b = b

    def predict(self, x):
        return (self.m*x) + self.b


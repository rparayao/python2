# Remi P 
# I&C SCI_X426.64 (FALL 2019/REG 00204/SEC 1) 
# Week 7 Assignment 11.15.2019



#Problem 1
#Write a function called list_is_in. This will take two arguments, 
# `list1` and `list2`.  It return a new list that is the same length as 
# list1, and contains True or False depending on if each item in the 
# list is found in list2 (see the example below). 
def list_is_in(list1, list2):
    '''checks if list1 is alos on list1'''
    newList = []
    index = 0
    for item1 in list1:
        same = False
        for item2 in list2:
            if item1 == item2:
                same = True
        newList.append(same)
        index = index + 1
    return newList



#Problem 2
#Write a function called mean_normalize. This function will take in an numpy array. 
# We will assume the array represents temperature data, where each column is 
# a different weather stations, and each row is an hourly temperature measurement.
def mean_normalize(input_array):
    '''Normalizes data from array'''
    mean = input_array - input_array.mean(axis=0)
    std = mean / mean.std(axis=0)
    return std


#Problem 3
#Write a class called temperature_model. The __init__ method will accept a filepath 
# to a csv file of numbers.  The __init__ load the file into a numpy array using 
# the loadtxt function from numpy (see the example below).
#class temperature_model:
class temperature_model:
    '''temperature model'''
    def __init__(self, filepath):
        self.filepath = filepath
       
# Remi P 
# I&C SCI_X426.64 (FALL 2019/REG 00204/SEC 1) 
# Week 2 Assignment 10.05.2019

import math

def count_uppercase_letters(my_string):
    ''' Counts the number of uppercase letters from the input string
    
    Parameters:
    -------
    my_string: string
        string to be counted for uppercase letters

    Returns:
    -------
    count : int
        the number of uppercase from my_string
    '''
    count = 0
    for string in my_string :
        if (string.istitle()):
            count = count + 1
    return count



def interleave_lists(list_1, list_2):
    '''Interleaves the elements from the two lists

    Parameters:
    -------
    list_1: list
        values from this lists will be interleaved
    list_2: list
        values from this lists will be interleaved

    Returns:
    -------
    newList: list
        interleave elements from list_1 and list_2
    '''
    newlist = []
    index = 0
    for __ in list_1:
        newlist.append(list_1[index])
        newlist.append(list_2[index])
        index = index + 1
    return newlist


def cylinder_stats(radius, height):
    '''Calculates the area and volume of cylinder

    Parameters:
    -------
    radius: int , float
        the radius of the cylinder
    height: int, float
        the height of the cylinder

    Returns:
    area: float
        the area of the cylinder
    volume
        the volume of the cylinder
    '''
    area = 2*math.pi*radius*(height + radius)
    volume = math.pi*(math.pow(radius,2))*height

    return area, volume
# Remi P 
# I&C SCI_X426.64 (FALL 2019/REG 00204/SEC 1) 
# Week 3 Assignment 10.12.2019

#Problem 1
#Write a function called all_the_kwargs. This function 
# will accept all the keyword arguments that are passed to it 
# and then return the number of keyword arguments that are passed
def all_the_kwargs(**kwargs):
    '''This function counts the number of all key words arguments'''
    count = 0
    for _ in kwargs:
        count = count + 1
    return count



#Problem 2
#Write a generator function called almost_fibonacci. 
# This function will accept one argument, N, and it 
# will produce the first N numbers of a sequence
def almost_fibonacci(num): 
    '''Prints the the sum of the first three number in the sequence'''
    prev_prev, prev, i = 0, 1, 1
    yield prev_prev
    yield prev
    for _ in range(num-2):
        yield i
        i, prev_prev, prev = i + prev + prev_prev, prev, i




#Problem 3
#Write a generator function called first_word_of_each_line. 
# This function will be very similar to the word count function 
# we went over in lecture
def first_word_of_each_line(filepath):
    '''prints the first word in each line'''
    with open(filepath, 'r') as my_file:
        for line in my_file:
            words = line.split()
            print(words[0])
          
                





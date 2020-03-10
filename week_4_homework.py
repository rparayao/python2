# Remi P 
# I&C SCI_X426.64 (FALL 2019/REG 00204/SEC 1) 
# Week 4 Assignment 10.19.2019


#Problem 1
#Write a function called raise_to_power. 
def raise_to_power(power):
    '''Raise numder to the power'''
    def raise_to_power2(num):
        result = num ** power
        return result
    return raise_to_power2


#Problem 2
#Using a closure, write a function called file_writer.
def file_writer(filepath):
    '''Returns a function that append to a file'''
    def file_append(text):
        '''writes text to file'''
        with open(filepath, 'a') as my_file:
            my_file.write(text)
    return file_append
        
#Problem 3
#This function accepts one argument, n, and it return 
#a generator function very similar to first_word_of_each_line
def word_n_of_each_line(n):
    '''prints the first word in each line'''
    def n_word_of_each_line(filepath):
        with open(filepath, 'r') as my_file:
            for line in my_file:
                words = line.split()
                if len(words) >= n:
                    yield words[n-1]
    return n_word_of_each_line
                


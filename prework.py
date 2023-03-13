# Write a function to print "Hello_USERNAME"--- 

def say_hello(user_name):
    print(user_name)

say_hello("Professor Falken")
          

# Question 2 write the odd numbers 1-100--- def first_odds():
"""Print the odd numbers from 1 - 100"""
number = 1
while number < 101:
    if number % 2 == 1:
        print(number)
        number += 1
    else:
        number += 1

            
# question three write a function that returns the max number among list. 
def max_number_in_list(a_list):
    max_number = max(a_list)
    return max_number

test = max_number_in_list([4,5,20,8,10])
print(test)

#   question  a function to return if the given year is a leap year
def is_leap_year(a_year):

    if a_year % 4 == 0:
        print("True")
    
    elif a_year % 100 == 0:
        print("False")
    
    elif a_year % 400 == 0:
        print("True")
    
    return a_year

is_leap_year(2016)

# question write function to check if all numbers in a list are consecutive
def is_consecutive(a_list):
 """ a function to check to see if all numbers in list are consecutive numbers """
 a_list_sorted=sorted(a_list)
 for i in range(1,len(a_list)):   
        if  a_list_sorted[i] ==  a_list_sorted[i-1] + 1:
            return True
        else:
            return False
    
print(is_consecutive(a_list=[2,3,5,4,6]))

#  Question write a function to check to see if all numbers in list are consecutive numbers 
def is_consecutive(a_list):
 a_list_sorted=sorted(a_list)
 for i in range(1,len(a_list)):   
        if  a_list_sorted[i] ==  a_list_sorted[i-1] + 1:
            return True
        else:
            return False
    
print(is_consecutive(a_list=[2,3,5,4,6]))
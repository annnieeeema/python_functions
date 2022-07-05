# Question 1
# Write a function named sum_to that accepts a single interger, n, and returns the sum of the integers from 1 to n. 

def sum_to(n):
    sum = list(range(n+1))
    i = 0 
    for num in sum: 
        i  = i + num
    print(i)

sum_to(4)
# answer: 10

# Question 2
# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list

def largest(list):
    new = 0
    for num in list: 
        if num > new: 
            new = num
    print(new)

list = [2, 4, 17, 6]
largest(list)
# answer: 17

# Question 3
# Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string. 
def occurances(strg1, strg2):
    sum = 0
    for letter in strg1:
        if strg2 == letter:
            sum = sum + 1
    print(sum)

occurances('doggydogworld', 'd')
# answer: 3

# Question 4
# Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. 

def product(*arbitrary):
    prod  = (arbitrary)
    group = 1
    for num in prod:
        group = group * num
    print(group)

product(1, 3, 9)
# answer: 27
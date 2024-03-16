# print('Welcome to python class')

''' 

Things to know about python programming
1. Open source
2. It is Versatile
3. It is a High level programming language
4. Object Oriented

'''

# Python Variables
'''
1. Variable Name

Rules guiding variable name declaration
i. It must be descriptive
ii. It must not start with any character except '_' and any alphabet
iii. A variable name declaration does not allow space inbetween the words
    you can use the following method to join them together
    a. snake casing
        my_first_name
    b. Pascal casing
        MyFirstName
    c. Camel casing 
        myFirstName



2. Assignment operator
3. Item/content

'''

containerOne = 'Water'
containerOne = 'Salt'
# print(containerOne)


first_name = 'Damilare'
last_name = 'Arise'
age = 10
occupation = 'Engineer'
hobby = 'Coding'
state_of_origin = 'Ekiti State'

# input function
# username = input('Username: ')
# print(f'My username is {username}')


# print('My name is',first_name)

'''
Assignment1
1. check for the different concatenating method we have in python
2. Use each of the methods to write about yourselve

'''


text1 = 'Today is my python class.'
text2 = 'I am so excited!'

# print(type(text2))

# Concatenation
'''
concatenation is the ability to join two or more python strings together
'''

# Method1: using the comma ','

first_name = 'Damilare'
last_name = 'Arise'
age = 10
# print('My name is',first_name,last_name,'. I am', age,'years old.')

# Method2: using the plus sign '+'

# print('My name is '+first_name+' '+last_name+'. I am '+str(age)+'years old')

# age = 20
# print('After 10years')

# print('My name is '+first_name+' '+last_name+'. I am '+str(age)+'years old')

# Method3: f string
# print(f'My name is {first_name} {last_name}. I am {age}years old.')


'''
        PYTHON DATATYPE
1. Text type; strings, str() e.g 'Banana', '55'

2. Number type;
    i.  integers, int() e.g 45, 6
    ii. float, float() e.g 45.4, 2.004
    iii. complex, complex() e.g 1 + 1j, 3 + 5j

3. Boolean type; bool(),  True == 1, False == 0

4. sequence type;
    i. list, list() e.g [25, 35, 56, 60], ['Banana', 'Adebayo', True, 45, 3 + 5j]
    ii. tuple, tuple() e.g (25, 35, 56, 60), ('Banana', 'Adebayo', True, 45, 3 + 5j)
    iii. range, range() e.g range(20)

5. mapping type;
    python dictionary; dict() e.g {'name':'Jesulayomi', 'matric_no':'DSE101'}

6. Set type; set() e.g {3, 5, 2, 6, 1, 4}, {'Bisola', 'Jesulayomi', 'Abimbola'}

7. Binary type; byte, bytearray, memoryview

'''

val = tuple(range(1,11,3))
# new_val = tuple(val)
# print(val)

student_detail = {'Name':'Jesulayomi', 'Matric_no':'DSE101', 'Fee': 20000}
# print(type(student_detail))
# print(student_detail['Fee'])

my_set = {3, 5, 2, 6, 1, 4}
set2 = {'Bisola', 'Jesulayomi', 'Abimbola'}
# print(my_set)
# print(set2)

"""
        Python Datatype conversion

    # convert from int, float, complex to string type
    # convert from list to tuple, set
    # convert from tuple to list, set
    # convert from set to list , tuple
"""

num = 45.6 + 1j
# print(f'Datatype before conversion {type(num)}')
# print(f'Datatype after conversion {type(str(num))}')

basket = ['rice', 'beans', 'yam']
# print(basket)
# print(f'Datatype before conversion {type(basket)}')
# print(f'Datatype after conversion {type(set(basket))}')
# print(set(basket))

# This is not convertible. hence it would throw a value error!
val = 'Damilare'
# print(int(val))



'''
    PYTHON OPERATORS
1. Arithmetic operator e.g +, -, *, **, /, //, %
2. Assignment operator e.g =, +=, -=, /=, //=, **=, *=, %=
3. Identity operator  e.g is, is not
4. comparison operator e.g ==, !=, >, <, >=, <=
5. Logical operator e.g and, or, not
6. Membership operator e.g in, not in
7. Bitwise operator e.g & , | , ~, ^, <<, >>
    # & 	AND	Sets each bit to 1 if both bits are 1
    # |	    OR	Sets each bit to 1 if one of two bits is 1
    # ^	    XOR	Sets each bit to 1 if only one of two bits is 1
    # ~ 	NOT	Inverts all the bits
    # <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
    # >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

    
 
'''
# floor division
# print(7 // 2)  # result = 3

# modulus
# print(7 % 2)   # result = 1 i.e the remainder

val = 3 

# val += 1 # val = val + 1
# print(val)

# identity operator
val2 = 4
# print(val is not val2)

# comparison operator
# print(val >= 3)

# LOGICAL OPERATOR

# conditional statement(if,else statement)

# A simple authentication app
# username = input('Username: ')
# password = input('Password: ')
# # print(username, password)
# if username == 'Damilare' or password == '1234':
#     print(f'Welcome {username}')
# else:
#     print('Invalid Login details')


basket = []


# if not basket: # is basket empty?
#     print('Basket is empty')
# else:
#     print('Basket is not empty')


ans = False
# if not ans: # is ans equal to False
#     print('Answer is false')
# else:
#     print('Answer is true')


# MEMBERSHIP OPERATOR
basket = ['rice', 'yam', 'ata rodo']

# print('gari' not in basket)



val = 20
bin_val = bin(20)
# print(bin_val)

fval = 45
sval = 36
# print(bin(45))
# print('45 = ',bin(fval))  #101101  
# print('36 = ',bin(sval))   #100100
# print('45 & 36 = ',bin(fval & sval)) # = 100100
# print('45 | 36 = ',bin(sval | fval)) # = 101101
# print('45 ^ 36 = ',bin(sval ^ fval)) # = 001001
# print(' ~ 45  = ', bin(~45)) # = 010010
# print('shift left = ',bin(sval << 2))
# print('shift right = ',bin(sval >> 2))

# Assigment
# Build a simple calulator app


# cafeteria app

# food = ['rice', 'beans']
# drink = ['coke', 'fanta']

# user_food = input('food: ')
# user_drink = input('drink: ')

# if user_food in food and user_drink in drink:
#     print(f'Take your {user_food} and {user_drink}')
# else:
#     print("We don't have what you want")


# ussd app

# user = input('Ussd code: ')
# if user == '*312#':
#     print('''
#             Welcome
          
#     1. data balance
#     2. buy data

#     ''')
# else:
#     print('Invalid ussd code')


#3rd, feb 2024

# correction to the Assigment
# Build a simple calulator app

# print('''
#         MyCalculator App

#     1. Addition Operation
#     2. Subtraction Operation
#     3. Division Operation
#     4. Exit

# ''')
# user = input('Choice: ')
# val1 = int(input('First Value: '))
# val2 = int(input('Second Value: '))

# if user == '1':
#     print(f'Answer: {val1 + val2}')
# elif user == '2':
#     print(f'Answer: {val1 - val2}')

# elif user == '3':
#     print(f'Answer: {val1 / val2}')

# elif user == '4':
#     print('logging out...')
#     exit()

# else:
#     print('Invalid option, Try again.')



# application that checks if a number is odd or even

# user = int(input('Your number: '))

# if user % 2 != 0:
#     print(f'{user} is an odd number')
# else:
#     print(f'{user} is an even number')


# ussd app

# user = input('Ussd code: ')
# if user == '*312#':
#     print('''
#             Welcome to MyMTN App
          
#     1. data balance
#     2. buy data

#     ''')
#     user = input('option: ')
#     if user == '1':
#         print('Your data balance is **** ')
#     elif user == '2':
#         print('''
#               Buy Data

#         1. Daily plan
#         2. Weekly plan
#         3. Exit
#         ''')

#         user = input('option: ')
#         if user == '1':
#             print('Daily plan')
#         elif user == '2':
#             print('Weekly plan')
#         elif user == '3':
#             print('logging out...')
#             exit()
#         else:
#             print('Invalid option, Try again.')

#     else:
#         print('Invalid option, Try again.')

# else:
#     print('Invalid ussd code')


# so we've covered if else statement, elif(for multiple condition) & nested if else statement


# Python strings

# Object: anything that has a property and can perform a function

# God is our creator as humans
# we humans are the creation ( see humans as a python object)
# dust was used to create us as humans (see dust as a python class)

text = 'hello Everybody I am an object object object from the Str class.'
# print(type(text))

Name = '--/&Dami lare' # ['D', 'a', 'm', 'i',' ', 'l', 'a', 'r', 'e']

# print(len(Name))
# print(Name[-1])
# ASCII
# print(chr(38))
# print(ord('&'))

# print(text.capitalize())
# print(text.title())
# print(len(text))
# print(text)
# print(text.strip())
# print(Name)
# print(Name.strip('--/&'))
# print(text.lower().strip())
# print(text.upper())

# text2 = text.split()
# print(text2)

# print('+'.join(text2))

# print(text.replace('Everybody', 'My people'))
# print(text.startswith('hello'))
# print(text.endswith('class.'))
# print(text.count('object'))
# print(text.index('Everybody'))
# print(text.center(100,'+'))


# user = input('yes or no: ').strip().lower()
# if user == 'yes':
#     print(f'your option is {user}')
# elif user == 'no':
#     print(f'your option is {user}')
# else:
#     print('Invalid option')

# Assignment
# create a simple CBT application
    

# escape characters

# \t  tab
# print('I am a\t\t\t genius')

# \b backspace
# print('I am a\b\b\b\b genius')

# \n  enter
# print('I am a\n\n genius')

# \r 
# print('I am a\r genius')

# print('C:\\online_class\\first_class.py')
# print(r'C:\online_class\first_class.py') # r means raw string

# CBT APP v1.0

# print('MyCBT APP'.center(100,'_'))

# score = 0

# Q1 = input('What is the capital of Nigeria\na) Abuja b) Lagos\nAns: ').strip()
# if Q1.lower() == 'a' or Q1.capitalize() == 'Abuja':
#     print('correct')
#     score += 5
# else:
#     print('Wrong')


# Q2 = input('What is the capital of Japan\na) Abuja b) Tokyo\nAns: ').strip()
# if Q2.lower() == 'b' or Q2.capitalize() == 'Tokyo':
#     print('correct')
#     score += 5
# else:
#     print('Wrong')



# print(f'Your total score is {score}')




# PYTHON COLLECTIONS
'''
        Types of python collections/array
    1. List
    2. Tuple
    3. Set
    4. Dictionary

'''

# Python LIST( [] or list())

'''
A list is a python collection type that is;
1. Indexed
2. Changeable or mutable
3. Ordered
4. It allows duplicate values
'''

item = ['rice', 'tomato', 'tomato', 'pepper', 'fish', 'ponmo', 1, 4.5, True, ['Bisola', 'Jesulayomi']]

# print(type(item))
# print(item[1])
# print(item[-1])
# print(item[1:4]) #Slicicng
# print(item[-3:-1])
# print(item[-1][0])

# item[3] = 'Egusi'
# print(item)
# item[0:3] = ['yam', 'potato', 'cocoa']
# print(item)

# Functions a List object can perform

# item.append('Car')
# item.append(['Car', 'House'])
# item.extend(['Car', 'House'])
# print(item.count('tomato'))
# print(item.index('ponmo'))
# item.pop()
# item.pop(5)
# item.reverse()
# item.remove('tyre')
# item.remove('tomato')
# item.insert(0,'yam')

# del item
# print(item)

# ASSIGNMENT 1
'''
learn about .sort

'''

names = ['Yemi', 'Pamilerin', 'Shola', 'Tolu']

# print(f'You are welcome {names[0]}')
# print(f'You are welcome {names[1]}')
# print(f'You are welcome {names[2]}')

#  For loop: It iterate over a sequence and strings

# for name in names:
#    print(f'You are welcome {name}') 

# x = 1
# name = 'Jesulayomi' 
# for letter in name:
#     print(f'{letter} - {x}')
#     x += 1

# Nested For Loop

# for name in names:
#     print(name)

#     for letter in name:
#         print(f' - {letter} ')

# for num in range(1, 7):
#     print(f'{num} Times Table')

#     for y in range(1, 13):
#         print(f'{num} x {y} = {num * y}')
             

# zip()

items = ['Bag', 'Jean', 'Shirt', 'Sneakers']
prices = [2000, 1000, 1500, 4000]


# for item, price in zip(items, prices):
#     print(f'{item} -- ${price}')


# CBT APP v2.0
    
# questions = [
#             '1. What is the capital of Nigeria\na) Abuja b) Lagos\n', 
#             '2. What is the capital of Ghana\na) Abuja b) Accra\n'
#         ]
# answers = ['a', 'b']

# score = 0

# for ques, ans in zip(questions, answers):
#     print(ques)
#     user = input('Answer: ').strip().lower()
#     if user == ans:
#         print('Correct\n')
#         score += 5
#     else:
#         print('Wrong')

# print(f'Your total score is {score}')


# Assignment 2
'''
Improving the Cbt application, do the following;

1. ask the user how many student are taking the test.
2. register all the student
3. call them one after the other to take the test
4. print out the student with the highiest score 
5. print the mean score.

'''
# print('My CBT test app'.center(100,'_'))

# students = []

# user = int(input('How many student are taking the test: '))
# for x in range(user):
#     student = input(f'Student name{x+1}: ')
#     students.append(student)

# ['femi', 'shola']
# # print(students)

# for each_student in students:
#     print(f'{each_student} is time for your test.')


#     # Exam questions
#     questions = [
#             '1. What is the capital of Nigeria\na) Abuja b) Lagos\n', 
#             '2. What is the capital of Ghana\na) Abuja b) Accra\n'
#         ]
#     answers = ['a', 'b']

#     score = 0

#     for ques, ans in zip(questions, answers):
#         print(ques)
#         user = input('Answer: ').strip().lower()
#         if user == ans:
#             print('Correct\n')
#             score += 5
#         else:
#             print('Wrong')

#     print(f'Your total score is {score}')

# score = [20, 30, 15]

# print(sum(score))
# print(len(score))
# print(max(score))


# Todo List v.1.0

# create Todo list
# add to do
# edit to do
# delete/remove an item in the todo list
# view to do list

# user = input('''
#         Welcome to MyTodo
             
#     1. create Todo
#     2. exit
             
# Option: ''')
# if user.strip() == '1':
#     mytodo = []
#     print('Todo list created successfully')

#     print('''
          
#     1. Add Todo
#     2. Edit Todo
#     3. Remove an item
#     4. View Todo
#     5. Exit
          
#     ''')

#     user = input('Option: ').strip() 
#     if user == '1':
#         print('You have only 5 slot for your todo list in this Version')
#         for x in range(5):
#             todo = input(f'Todo-{x}: ')
#             mytodo.append(todo)
        
#         print('''
#         1. Edit todo
#         2. View todo
#         ''')
#         user = input('Option: ').strip() 
        
# elif user.strip() == '2':
#     exit()
# else:
#     print('Invalid Option')



# 2. Tuple (), tuple()
item = ('rice', 'tomato', 'tomato', 'pepper', 'fish', 'ponmo', 1, 4.5, True, ['Bisola', 'Jesulayomi'])
# print(type(item))

'''
Properties of a class tuple
1. unchangeable/immutable
2. It can be indexed
3. it accepts duplicate values
4. Ordered

'''

# print(item)
# print(item[1])
# print(item[-1])
# print(item[1:4])
# print(item[:4])

# item[0] = 'Yam'
# print(item)

# new_item = list(item)
# new_item[0] = 'Yam'
# item = tuple(new_item)
# print(item)

# UNPACKING
# print(item)
# *val, = item
# print(val)

names = ('shola', 'ade', 'femi', 'lola')
# print(names)
# x,y,z,v = names
# print(x)
# print(y)
# print(z)
# print(v)


# Functions a class tuple can perform

# print(item.index('ponmo'))
# print(item.count('tomato'))


# details = [('ade@gmail.com', 1234), ('lola@gmail.com', 1234)]

# for email, password in details:
#     # print(email)
#     print(password)


# test = [
#     ('1. What is the capital of Nigeria\na) Abuja b) Lagos\n', 'a'),
#     ('2. What is the capital of Ghana\na) Abuja b) Accra\n', 'b')
# ]


# for ques, ans in test:
#     print(ques)
#     user = input('ans: ')
#     if user == ans:
#         print('correct')


# 3 SET {} or set()
'''
    Properties
1. it is not ordered
2. it does not accept duplicate value
3. it is unchangeable
4. it is unindexed
'''

myset = {'apple', 'banana', 'orange', 'water-melon', 'apple'}
# print(type(myset))
# print(myset)
# print(myset[1]) #this will result to an error



# SET FUNCTIONS
# myset.add('strawberry')
# myset.add({'Ade','Femi','Shola'}) #this will result to an error
# myset.update(['Ade','Femi','Shola'])
# myset.discard('carrot') #This would not throw error
# myset.remove('carrot') #This would throw error

'''Guess game'''
# print(myset)
# val = myset.pop()
# user = input('Your guess: ').strip().lower()
# # print(myset)
# if user == val:
#     print('You guessed right')
# else:
#     print(f'Your are wrong, the right guess is {val}')

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9,12}
set2 ={3, 5, 2, 12}

set3 = {2, 4, 7, 8}

# print(set1)
# print(set2)
# print(set3)
# print(set4)

# print(set1.difference(set2))
# set4 = set1 - set2

# set4 = set1.union(set2)
# intersect = set1.intersection(set2)
# intersect = set1.intersection(set2).intersection(set3)
# set1.intersection_update(set2)
# set4 = set1.symmetric_difference(set2) 
# print(set1.difference(set2))

# set2.symmetric_difference_update(set1)
# set4 = set1.difference(set2)
# print(set1.isdisjoint(set2)) # The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
# print(set1.issuperset(set2))
# print(set1.issubset(set2))
# print(set3)
# print(set2)
# print(intersect)
# print(set4)
# print(set1)


# 4. Dictionary {key:value} or dict(key=value)
'''
    Properties
1. it does not allows duplicate item
2. it is changeable
3. it is ordered
'''
car = {
    'Model':'Lexus 350', 
    'Year':'2020', 
    'Color':['Black','Blue'], 
    'Year2':'2020',
    'Owner':{
        'Name': 'Mr. Damilare',
        'Amount': 3_000_000
    } 
    }
# print(type(car))
# print(car)
# print(car['Model'])
# print(car['Owner']['Amount'])


# [], (), {}, {key:value}

# car['Model'] = 'Lexus 370'
# car['Owner']['Name'] = 'Miss Bisola'
# print(car)

#FUNCTIONS
# print(car.keys())
# for key in car.keys():
#     print(key)

# print(car.values())
# for val in car.values():
#     print(val)

# print(car.items())
# for key, value in car.items():
#     print(f'{key} = {value}')



# test = {
#     'b':'1. What is the capital of Lagos a. Abuja b. Ikeja',
#     'b': '2. What is the name of the president of Nigeria a. Buhari b. BAT'
# }
# for ans, quest in test.items():
#     print(quest)
#     user = input('Ans: ').strip().lower()
#     if user == ans:
#         print('correct✅')
#     else:
#         print('Wrong❌')


# store_db = {
#     'Chelsea boot': 40000,
#     'Round neck': 5000,
#     'Belt': 4000
# }

# print(store_db.items())

# x = 1

# products = []
# prices = []

# # print(' Our available Items are;')
# for item, price in store_db.items():
#     print(f'''
#         {x}. {item} - #{price}''')
    
#     products.append(item)
#     prices.append(price)
#     x+=1
    
# item =input('What Item are you buying: ').strip().capitalize()
# if item in products:
#     index_item = products.index(item)
# #     # print(index_user)
#     price = prices[index_item]

#     print(f'{item} is avaliable and it cost #{price}')
    
# else:
#     print(f'{item} unavailable at the moment')
# print(store_db.values())



# Other functions 
store_db = {
    'Chelsea boot': 40000,
    'Round neck': 5000,
    'Belt': 4000
}

# store_db.clear()
# print(store_db.get('Chelsea booth', 'Not found'))
# print(store_db['Chelsea booth'])
# store_db.pop('Belt')
# store_db.popitem()
# store_db.update({'Sneakers':50000, 'Jean':10000})
# print(store_db)



# WHILE LOOP

# While loop iterate base on a condition

# x = 10
# while x > 0:
#     print(f'You are welcome {x}')

#     x -= 1


# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down and pass it around, 98 bottles of beer on the wall
    
# beer = 99
# while beer >= 1:
#     print(f'{beer} bottles of beer on the wall, {beer} bottles of beer.')
#     beer -= 1
#     print(f'Take one down and pass it around, {beer} bottles of beer on the wall')
    

# ussd = input('USSD: ').strip()
# if ussd == '*312#':
#     print('1. Buy data\n2. Check balance')
# else:
#     print('invalid code')

# ussd = input('USSD: ').strip()
# while ussd != '*312#':
#     print('invalid code')
#     ussd = input('USSD: ').strip()
# else:
#     print('1. Buy data\n2. Check balance')


# x = 10
# while x > 0:
#     print(x)
#     x-=1

#     if x == 5:
#         break


# x = 10
# while x > 0:
#     x-=1
#     if x == 5:
#         continue
    
#     print(x)

# ticket = 10
# while ticket > 0:
#     age = int(input('age: '))
#     if age < 18:
#         print('You are too young')
#         continue
#     else:
#         print(f'Take your ticket {ticket}')
    
#     ticket -= 1



# PYTHON FUNCTIONS

'''
3stages undergone while working with python function
1. Function declaration
2. Function Definition
3. Function Invocation

types of function
1. Parametized
2. Unparametized
'''

# ''.capitalize()
''.center(100, '#') 

# Unparametized function

# def add():
#     print(2 + 2) 

# add()

# Parametized function

# def add(a , b = 10):
#     print(a + b)

# add(a = 10)

# add(10, 20)


# def add(a:float, b: float = 10):
# #     '''
# #     It prints out the addition of two values
# #     '''

# #     print(a + b)

# # add(a = 2, b = 3)


# def add(a, b):
#     return a + b

# add(10, 5)

# result = 20 * add(2, 3)
# print(result)

# def add()
    
# def add(val1:int, val2:int = 10):
#     '''
#     This Function adds two together\n
#     it print out val1 + val2

#     '''
#     # print(val1 + val2)
#     return val1 + val2


# def exp():
#     ans = 2 ** add(20)
#     return ans

# def discribe(name):
#     print(f'{name}, Your answer is {exp()}')


# discribe(name='Damilare')

# LOCAL AND GLOBAL VARIABLE

# val1 = int(input('value1: '))
# val2 = int(input('value2: '))

# def add():
#     global add_var
#     add_var = 50
#     print(val1 + val2 + add_var)

# def sub():
#     print(val1 - val2 + add_var)

# add()
# sub()



def home():
    print('Welcome to my alata calculator')
    global value1
    global value2
    value1 = float(input('Value 1: '))
    value2 = float(input('Value 2: '))

    user = input('''      
    Choose your operation;
                 
    1. Addition 
    2. Subtraction
    #. Exit      
          
    : ''')


    if user == '1':
        addition()
    elif user == '2':
        subtraction()
    elif user == '#':
        exit()
    else:
        print('Invalid option')
        home() # Recursive



def addition():
    print(f'Your answer is {value1 + value2}')
    decide()
    

def subtraction():
    print(f'Your answer is {value1 - value2}')
    decide()
    

def decide():
    user = input('Press 1 to repeat: ')
    while user == '1':
       home()
    else:
        exit()
    

# home()

'''
ASSIGNMENT

1. Add more functions to the above calculator code
2. Using the function approach, build a ussd app

DOWNLOAD AND INSTALL XAMMP
'''


'''
OOP - Object Oriented Programming

'''




class Calculator:
    def __init__(self):
        self.name = 'Casio'
        self.production_date = 2020

        self.title()

    def title(self):
        print(f'This is a {self.name} calculator, produced in year {self.production_date}')
        self.home()

    def home(self):
        print('Welcome to my alata calculator')
        
        self.value1 = float(input('Value 1: '))
        self.value2 = float(input('Value 2: '))

        user = input('''      
        Choose your operation;
                    
        1. Addition 
        2. Subtraction
        #. Exit      
            
        : ''')


        if user == '1':
            self.addition()
        elif user == '2':
            self.subtraction()
        elif user == '#':
            exit()
        else:
            print('Invalid option')
            self.home() # Recursive

    def addition(self):
        print(f'Your answer is {self.value1 + self.value2} in calculator {self.name}')

    def subtraction(self):
        print(f'Your answer is {self.value1 - self.value2} in calculator {self.name}')  


# mycalc = Calculator()


# mycalc.name = 'Porpo'
# print(mycalc.name)

# mycalc.title()
        


class Entrance:
    def __init__(self):
        self.company_name = 'SQI College Of ICT'
        self.staffs_db = [
            ('012','Ade Ade'),
            ('014', 'Femi Femi')
        ]

        self.students_db = [
            ('234', 'John Mark', 'Fully Paid'),
            ('222', 'Tomi Tomi', 'Half Paid'),
            ('345','Tolu Tolu', 'No Payment')
        ]

        self.home()

    def home(self):
        user = input(f'''
            Welcome to {self.company_name}

        Kindly verify your Identity
        1. Student
        2. Staff
        3. Visitor
    
        Option: ''').strip()

        if user == '1':
            self.student_page()
        elif user == '2':
            self.staff_page()
        elif user == '3':
            self.visitor_page()
        else:
            user = input('Invalid option. press # to exit or 1 to retry: ').strip()
            if user == '1':
                self.home()
            else:
                exit()


    def student_page(self):
        pass

    def staff_page(self):
        pass
    
    def visitor_page(self):
        pass



# enter = Entrance()
# enter.home()


'''
        ASSIGNMENT
1. Finish the entrance application above using OOP approach
2. Build a Ussd app using OOP approach
'''

# INHERITANCE & PYTHON MODULARIZATION


class Parent:
    def __init__(self, x):
        self.lastname = x
        self.firstname = 'John'
        self.hobby = 'Playing football'

        # self.brief()

    def brief(self):
        print(f'My name is {self.lastname} {self.firstname},  I love {self.hobby}')


father = Parent('Ojo')
# print(father.firstname)
# father.brief()


class Child(Parent):
    def __init__(self, x):
        super().__init__(x)
        #Or
        # Parent.__init__(self, x)

        self.firstname = 'Peter'
        self.hobby = 'Swimming'
        self.height = '5.4ft'

        self.describe()
    
    def describe(self):
        print(f'My name is {self.lastname} {self.firstname},  I love {self.hobby}. I am {self.height} tall')

# first_born = Child('Ojo')
# print(first_born.firstname)
# first_born.brief()



class UBA:
    def __init__(self):
        self.name = 'UBA'
        self.Branch = 'HQrts'

        # self.home()
        
    def home(self):
        print(f'''
                Welcome to {self.name} {self.Branch}
        
        1. Sign in 
        2. Sign up

        ''')

# headbranch = UBA()
# headbranch.home()

class FirstBranch(UBA):
    def __init__(self):
        # super().__init__()
        # or
        UBA.__init__(self)
        self.Branch = 'Lagos Branch'

    def gen_otp(self):
        print('I would be able to generate otp')

# lagos = firstBranch()
# lagos.home()
# lagos.gen_otp()



class FirstBranch_sub1(FirstBranch):
    def __init__(self):
        super().__init__()
        self.Branch = 'Ikeja Lagos'

ikeja = FirstBranch_sub1()
# ikeja.gen_otp()
ikeja.home()


"""
1. script : A single file that has a set programs inside of it
2. Modules : it is a script with One or more classes inside
3. Library : They are a folder with different modules inside

"""

# SQL 1 Database
# Error handling
# File handling
# Regular expression
# python date time
# pymath
# ipython 
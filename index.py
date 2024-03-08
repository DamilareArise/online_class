"""
# name = 'Joshua'
print(name)

"""

# print("it's mine")
# x = 22
# print(x + 2)

# basket = ['yam','rice',34,34, 4.5, True, False]
# basket[0] = 'isu'

# basket = ('yam','rice',34,34, 4.5, True, False)
# basket[0] = 'isu'
# print(basket)

# x = range(1,20)
# y = tuple(x)
# print((y))

# basket = {'yam','rice',34,34, 4.5, True, False}
# print(basket)         

# student = {'name':'Joshua','sex':'Male'}
# print(student['sex'])

# x = ''
# y = 4
# print(x == 5)
# if not x:
#     print('Yes')
# else:
#     print('No')

# x = bin(10)
# print(x)

# name = input('answer: ')
# if name == 'dare':
#     print('welcome',name)
# elif name == 'Dare':
#     print('welcome',name)
# elif name == 'DARE':
#     print('welcome',name)
# else:
#     print('null')

ussd = input('USSD Code: ')
if ussd == '*312#':
    print('''
        1. Check balance
        2. Buy data

        ''')
    user = input('Option: ')
    if user == '1':
        print('Your balance is ****')
    elif user == '2':
        print('''
        1. Daily plan
        2. Weekly plan
        ''')
    else:
        print('Invalid Option')


elif ussd=='*141#':
    print('''
        1. *310# check balance
        2. *312# Buy data

        ''')

else:
    print('Invalid USSD code')
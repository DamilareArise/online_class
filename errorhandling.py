'''
Two Types of error
1. compile type error
2. runtime error
'''
#     container=''
# print(container)

# li = [1, 2, 4, 6]
# print[li[7]]

'''
These syntax help us handle our errors

try
except
else
finally
'''

# container = ''
# try:
#   print(container)  
# except:
#   print('There is an error oo. ')
# else:
#   print('You are seeing me becuase there is no error')
# finally:
#   print('I would show if there is an error or not')


# val1 = float(input('Val 1: '))
# val2 = float(input('Val 2: '))
# print(val1+val2)


def add():
    try:
        val1 = float(input('Val 1: '))
        val2 = float(input('Val 2: '))
    except:
        print('There is an error')
        add()
    else:
        print(f'Result = {val1+val2}')

# add()
        

def add():
    try:
        val1 = float(input('Val 1: '))
        val2 = float(input('Val 2: '))
        val1/val2
    except ValueError as v:
        print(v)
        add()

    except ZeroDivisionError as z:
        print('Your divisor can not be Zero')
        add()

    except Exception as e:
        print(e)
        add()


    else:
        print(f'Result = {val1+val2}')

# add()
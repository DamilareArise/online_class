''''
ASSIGNMENT
1. Build an Entrance app for SQI
    i. Create a database for staff and student using the list of tuple approach
    ii. verify identity(Staff, Student, Vistor) and authenticate.
'''

staffs_db = [
    ('012','Ade Ade'),
    ('014', 'Femi Femi')
]

students_db = [
    ('234', 'John Mark', 'Fully Paid'),
    ('222', 'Tomi Tomi', 'Half Paid'),
    ('345','Tolu Tolu', 'No Payment')
]

user = input('''
    Welcome to SQI College Of ICT
Kindly verify your Identity
1. Student
2. Staff
3. Visitor

Option: ''')

student_id = []
student_name = []
payment_status = []

for id, name, payment in students_db:
    student_id.append(id)
    student_name.append(name)
    payment_status.append(payment)

# print(student_id, student_name, payment_status)

if user == '1':
    id = input('Your student ID: ').strip()
    if id in student_id:
        _index = student_id.index(id)
        name = student_name[_index]
        payment = payment_status[_index]
        # print(_index)

        print(f'Welcome {name}, Kindly wait lets verify your payment status...')
        if payment == 'Fully Paid':
            print('Access granted you\'ve completed your payment')
        elif payment == 'Half Paid':
            print('Access granted, Kindly make sure you complete your fee as soon as possible.')
        else:
            print('Access denied. Visit the front desk to make payment. ')


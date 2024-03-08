'''
Improving the Cbt application, do the following;

1. ask the user how many student are taking the test.
2. register all the student
3. call them one after the other to take the test
4. print out the student with the highiest score 
5. print the mean score.

'''

'''1. ask the user how many student are taking the test.'''
number_student = int(input('''
            Welcome to myCBT
             
Kindly supply the numbers of student taking your test: '''))


'''2. register all the student'''
student_db = []
for x in range(number_student):
    student_name = input(f'Student name{x+1}: ')
    student_db.append(student_name)
    
# print(student_db)
'''3. call them one after the other to take the test '''

students_score = []

for student in student_db:
    print(f'\n{student}, It is time for your test.\n')

    '''The test'''

    questions = [
            '1. What is the capital of Nigeria\na) Abuja b) Lagos\n', 
            '2. What is the capital of Ghana\na) Abuja b) Accra\n'
        ]
    
    answers = ['a', 'b']
    score = 0

    for quest, ans in zip(questions,answers):
        print(quest)
        user = input('Answer: ').strip().lower()
        if user == ans:
            print('Correct')
            score +=5
        else:
            print('Incorrect')
    
    print(f'\n{student}, your total is {score}')
    students_score.append(score)

print('\nAll the student are done taking the test\n')
# print(student_db)
# print(students_score)

print('''
        Result Sheet
    STUDENT ---> SCORE
''')
for student, score in zip(student_db,students_score):
    print(f'''
    {student} ---> {score}''')    

'''4. print out the student with the highiest score '''
max_score = max(students_score)
print(f'The maximum score is {max_score}')
index_max_score = students_score.index(max_score)
print(f'The student with the maximum is {student_db[index_max_score]}')

'''5. print the mean score.'''
mean_score = sum(students_score)/len(students_score)
print(f'The mean score is {mean_score}')

[
    ('studentname', 'Paid'),
]

''''
ASSIGNMENT
1. Build an Entrance app for SQI
    i. Create a database for staff and student using the list of tuple approach
    ii. verify identity(Staff, Student, Vistor) and authenticate.
'''
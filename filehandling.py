myfile = open(r'C:\online_class\mycbt.py')
# print(myfile.read())

'''
MODE
r = read only
w = Write 
a = append
x = create

'''

# myfile = open(r'C:\online_class\file1.txt', mode='w')
# myfile.write('Hello this is python level to class')


# myfile = open(r'C:\online_class\file1.txt', mode='a')
# myfile.write('\nHello this is python level to class')

# myfile = open(r'C:\online_class\file2.pdf', mode='x')

# file = open(r'C:\online_class\file1.txt', 'r')
# print(file.read())
# file.close()
# print(file.read())


# with open(r'C:\online_class\file1.txt', 'r') as myfile:
    # print(myfile.readlines())
    # for line in myfile.readlines():
    #     print(line) 
    
# with open(r'C:\online_class\pythonclass.py', mode='r', encoding='utf8') as myfile:
#     print(myfile.read())


file = open(r'C:\online_class\president_height.csv', mode='r')
# print(file.read())
details = file.readlines()
details.pop(0)
# print(details)
names = []
heights = []

for each in details:
    detail = each.split(',')
    names.append(detail[1])
    height = detail[2].strip('\n')

    heights.append(int(height))

    # print(detail[2])

print(names)
print(heights)
'''
Assignment
1. get the president with thwe max and min height
2. using the file student_grade, seperate the studdents with grade A,b,and C to a seperate file respectively
'''
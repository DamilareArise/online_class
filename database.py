'''
structured data/tabular data
unstructered data

sql - structured query language
mysql
postgreSql
MSSQl
Oracle
Sqllite


NOSQL - unstructered
{
name:Ojo Ade

}

MongoDB



relationship between tables
1. onetoone relationship
2. onetomany relationship
3. manytomany relationship
'''
# pip install mysql_connector

import mysql.connector as sql

# mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '')
mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database = 'example2_db')

mycursor = mycon.cursor()
mycon.autocommit = True
# mycon.disconnect()

# query = 'CREATE DATABASE example2_db'
# mycursor.execute(query)

# mycursor.execute('SHOW DATABASES')

# for db in mycursor:
#     print(db)

# query = 'CREATE TABLE customer_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(30), email VARCHAR(30) UNIQUE, account_no VARCHAR(10) UNIQUE, account_bal FLOAT(10), date_time DATETIME DEFAULT CURRENT_TIMESTAMP)'

# mycursor.execute(query)


# mycursor.execute('SHOW TABLES')

# for table in mycursor:
#     print(table)


# query = 'ALTER TABLE customer_table CHANGE id customer_id INT(4) AUTO_INCREMENT'
# query = 'ALTER TABLE customer_table ADD password VARCHAR(30)'
# mycursor.execute(query)


query = "INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES('Arise Damilare', 'dami@gmail.com', '123456789', 25000, '1234')"

# mycursor.execute(query)
# mycon.commit()


# query = "INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES(%s, %s,%s, %s, %s)"

# values = ('Arise Tolu', 'tolu@gmail.com', '123445789', 25000, '1234')

# mycursor.execute(query, values)
# # mycon.commit()
import random


def signup():
    name = input('Full name: ')
    email = input('Email: ')
    account_no = random.randint(2100000000, 2199999999)
    account_bal = 0
    password = input('preferred password: ')
    
    query = 'INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES(%s, %s, %s, %s, %s)'
    val = (name, email, account_no, account_bal, password)
    mycursor.execute(query,val)
    print('Account has been created succesfully')

# signup()
    
# SELECT QUERY

# query = 'SELECT * FROM customer_table'
# mycursor.execute(query) 
# details = mycursor.fetchall()
# print(details[0][3])
    
# query = 'SELECT * FROM customer_table WHERE email="dami@gmail.com"'
# mycursor.execute(query) 
# details = mycursor.fetchone()
# print(details)
    
# email = input('Email: ')
# query = 'SELECT * FROM customer_table WHERE email=%s'
# val = (email,)
# mycursor.execute(query, val) 
# details = mycursor.fetchone()
# print(details)

def login():
    email = input('Email: ')
    password = input('Password: ')
    query = 'SELECT fullname, account_no, account_bal FROM customer_table WHERE email=%s AND password = %s'
    val = (email,password)
    mycursor.execute(query, val) 
    details = mycursor.fetchone()
    
    if details:
        print('You have successfully login')
        print(details)
    else:
        print('Incorrect email or password')

# login()
        

# UPDATE QUERY
        
def reset_password():
    email = input('Email: ')
    new_password = input('New password: ')
    query = 'UPDATE customer_table SET password=%s WHERE email=%s'
    val = (new_password, email)
    mycursor.execute(query,val)
    print('Password rest successful')

# reset_password()

# DELETE QUERY
     
# query = 'DELETE FROM customer_table WHERE customer_id = 2'
# mycursor.execute(query)
# print('user deleted succesfully')
    
# TRUNCATE QUERY
# query = 'TRUNCATE TABLE customer_table'
# mycursor.execute(query)
    
# DROP query
# mycursor.execute('DROP TABLE customer_table')
# mycursor.execute('DROP DATABASE example2_db')
    

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


query = "INSERT INTO customer_table(fullname, email, account_no, account_bal, password) VALUES(%s, %s,%s, %s, %s)"

values = ('Arise Tolu', 'tolu@gmail.com', '123445789', 25000, '1234')

mycursor.execute(query, values)
# mycon.commit()
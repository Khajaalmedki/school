import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='jacs5455JACS%$%%'
)

cursor = mydb.cursor()

try:
    cursor.execute('create database school_management;')
    cursor.execute('use school_management;')
except:
    cursor.execute('drop database school_management;')
    cursor.execute('create database school_management;')
    cursor.execute('use school_management')

cursor.execute('create table student_info(student_name varchar(30), father_name varchar(30), mother_name varchar(30), date_of_birth varchar(15), date_of_joining varchar(15), mobile_number varchar(20));')
mydb.commit()

while input('Would like to register a student? :') != 'No':
    students_name = input('Student Name: ')
    fathers_name = input('Fathers Name: ')
    mothers_name = input('Mothers Name: ')
    date_of_birth = input('Date of Birth: ')
    date_of_joining = input('Date of Joining: ')
    mobile_number = input('Mobile Number: ')

    # Entering data in mysql table
    sql_query = """insert into student_info values('{}', '{}', '{}', '{}', '{}', '{}');""".format(str(students_name), fathers_name, mothers_name, date_of_birth, date_of_joining, mobile_number)
    cursor.execute(sql_query)
    mydb.commit()

mydb.close()

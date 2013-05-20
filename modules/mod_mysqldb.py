#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Mod: mysqldb module
'''


import MySQLdb as mysql


#==========================================================================================
#
#  MySQL-python
#     It is an interface to MySQL that:
#
#       - Compliance with Python db API 2.0 [http://www.python.org/dev/peps/pep-0249/]
#       - Thread safety
#       - Thread-friendliness (threads will not block each other)
#
#    MySQL-3.23 through 5.5 and Python-2.4 through 2.7 are currently supported.
#
#==========================================================================================


# let's create a testing database
# CREATE DATABASE IF NOT EXISTS mod_mysqldb DEFAULT CHARACTER SET 'UTF8' DEFAULT COLLATE 'UTF8_GENERAL_CI';
# GRANT ALL PRIVILEGES ON mod_mysqldb.* TO 'user'@'localhost' IDENTIFIED BY 'user';


# let's connect to our database

conn = mysql.connect('localhost', 'user', 'user', 'mod_mysqldb')
cursor = conn.cursor()


#==========================================================================================
#
#  Inserting
#
#==========================================================================================


cursor.execute("CREATE TABLE IF NOT EXISTS writers(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25), UNIQUE KEY (name));")
cursor.execute("INSERT IGNORE INTO writers(Name) VALUES('Jack London')")
cursor.execute("INSERT IGNORE INTO writers(Name) VALUES('Honore de Balzac')")
cursor.execute("INSERT IGNORE INTO writers(Name) VALUES('Lion Feuchtwanger')")
cursor.execute("INSERT IGNORE INTO writers(Name) VALUES('Emile Zola')")
cursor.execute("INSERT IGNORE INTO writers(Name) VALUES('Truman Capote')")


# let's insert them using a list

more_writers = ['Yukio Mishima', 'Lev Tolstoi', 'Franz Kafka']
for writer in more_writers:
    cursor.execute("INSERT IGNORE INTO writers(Name) VALUES(%s)", writer)


more_writers_using_many = ['Charles Bukowski', 'Jorge Luis Borges', 'Gabriel Garcia Marquez']
cursor.executemany("INSERT IGNORE INTO writers(Name) VALUES(%s)", more_writers_using_many)


# WARNING: executemany just makes a loop on execute, so it is not a bulk update


more_writers_using_dict = [{'name':'Pablo Neruda'}, {'name':'Fedor Dostoievski'}]
cursor.executemany("INSERT IGNORE INTO writers(Name) VALUES(%(name)s)", more_writers_using_dict)

cursor.execute("INSERT IGNORE INTO writers(Name) VALUES(%s)" % 'Francis Scott Fitzgerald')


#==========================================================================================
#
# WHAT HAS HAPPENED?
#
#==========================================================================================

"INSERT IGNORE INTO writers(Name) VALUES(%s)" % 'Francis Scott Fitzgerald'


# It is recommend to interpolate sql using the DB API.
# It knows how to deal with strings, integers, booleans, None...


#==========================================================================================
#
#  Querying
#
#==========================================================================================


cursor.execute('SELECT * FROM writers')
for writer in cursor.fetchall():
    print writer


# query for an specific register
cursor.execute("SELECT * FROM writers WHERE name='Pablo Neruda'")
print cursor.fetchone()


# querying using interpolation
cursor.execute("SELECT * FROM writers WHERE name=%(name)s", {'name': 'Charles Bukowski'})
print cursor.fetchone()


# using a dict cursor to improve working with a queryset
import MySQLdb.cursors
cursor.close()
conn.close()
conn = mysql.connect('localhost', 'user', 'user', 'mod_mysqldb', cursorclass=MySQLdb.cursors.DictCursor)
cursor = conn.cursor()

cursor.execute('SELECT * FROM writers')
for writer in cursor.fetchall():
    print writer

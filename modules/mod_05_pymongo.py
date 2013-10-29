#-*- coding: utf-8 -*-
u"""
MOD: pymongo
"""


import pymongo


#===============================================================================
# 'pymongo' is the official Python MongoDB driver
#===============================================================================


#==========================================================================================
#
# Let's connect to our database
#
#==========================================================================================



client = pymongo.MongoClient('localhost', 27017)  # localhost:27017 is the default value
dbconn = client.mod_pymongo  # also client['mod_pymongo'] getting a database is so easy ('use db' in mongo shell)
# db.authenticate(username, password)  # Not enabled in our db right now

dbconn.writers.drop()

#===============================================================================
# - When connecting you can provide a list of seeds (replica set servers) in several ways
#    - http://api.mongodb.org/python/current/examples/high_availability.html
#===============================================================================

# Now we create another client to a replicaset 'sdrepl' with three members
# To follow this part, follow the instructions to create a replica set with three members in
# See https://github.com/pablito56/pycourse/wiki/Replicaset-Config to create locally 

from pymongo import ReadPreference
from pymongo.errors import AutoReconnect, ConnectionFailure, DuplicateKeyError
replica_client = pymongo.MongoClient(
                ('localhost:27017', 'localhost:27018', 'localhost:27019'), # also you can use url format
                w=3, # globally set write_concern (wtimeout can also be set...).
                replicaset='sdrepl',
                read_preference=ReadPreference.PRIMARY, # several options available
                auto_start_request=True  # consistent reads (socket allocated by requests)
                ) # you can also use MongoReplicaSetClient
# More options in http://api.mongodb.org/python/current/api/pymongo/connection.html

# When some of the hosts can not be accessed AutoReconnect is raised (still can use replica_client)
# When none of the hosts can be accessed, ConnectionFailure will be launched (must exit)

db_replica = replica_client.mod_pymongo
db_replica.books.drop()

#==========================================================================================
#
#  Inserting
#
#==========================================================================================


dbconn.writers.ensure_index([("name", pymongo.ASCENDING), ("age", pymongo.DESCENDING)], unique=True, name="unique_name")
dbconn.writers.insert({"name": "Jack London", "age": 200})
dbconn.writers.insert({"name": "Honore de Balzac", "age": 300})
dbconn.writers.insert({"name": "Lion Feuchtwanger", "age": 400})  # Note that the collection is created on demand
dbconn.writers.insert({"name": "Truman Capote", "age": 102})  # ObjectId (_id field value) is returned

# ensure_index can use kw cache_for and the driver will cache the index creation
# create_index in pymongo call internally ensure_index (no cache here). create_index is deprecated in shell


# let's insert them using a list

more_writers = ["Yukio Mishima", "Lev Tolstoi", "Franz Kafka", "J. D. Salinger"]
for writer in more_writers:
    dbconn.writers.insert({"name": writer, "age": 90})


more_writers_using_bulk = ["Charles Bukowski", "Jorge Luis Borges", "Gabriel Garcia Marquez"]
dbconn.writers.insert([{"name": name} for name in more_writers_using_bulk])

# some in replica_set
db_replica.books.insert({'_id': 'hobbit', 'editions': []}) # rules is pretended to be a list of complex objects
db_replica.books.insert({'_id': 'lord_rings', 'editions': None }, w=0)  # write_concern can be disabled in collection level operations

from pymongo.errors import DuplicateKeyError, OperationFailure

# collection level operations raise OperationFailure when a problem happens
# OperationFailure is translated in some cases:

try:
    db_replica.books.insert({'_id': 'hobbit'})
except DuplicateKeyError:
    print "Already created object"
except OperationFailure:
    print "Some problem occurred" 

# Most of shell operations can be translated easilly:
# dict and list in python vs object and array in json
# some times dict must be changed to list of set because dict has no ordering... (ensure_index)

#==========================================================================================
#
#  Querying
#
#==========================================================================================


cursor = dbconn.writers.find()
for writer in cursor: # we get a pymongo Cursor not a list (ordering, skip...)
    print writer


# query for an specific register
res = dbconn.writers.find_one({"name": "Pablo Neruda"})
print res # we get a dict in python

cursor = dbconn.writers.find({"name": "Pablo Neruda"})
for writer in cursor:
    print writer
    
# querying with several fields, just provide a dict
import re
dbconn.writers.insert({'name': 'Miguel de Unamuno', 'age': 130})
dbconn.writers.insert({'name': 'Miguel Delibes', 'age': 90})
dbconn.writers.insert({'name': 'Miguel de Cervantes', 'age': 500})
res = dbconn.writers.find({"name": re.compile("^Miguel"), "age": {'$lt': 200}}) # regex can be used in query
print list(res) # we get a dict in python


# sort, skip and limit are quite similar to shell
res = dbconn.writers.find().sort('name', pymongo.DESCENDING).skip(3).limit(1)
print list(res)

# you can use it as kw arguments
res = dbconn.writers.find(skip=3).sort('name', pymongo.DESCENDING).limit(1)
print list(res)


# to sort by more than one parameter we use list of set not dict 
res = dbconn.writers.find().sort([('name', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)]).skip(3).limit(1)
print list(res)

# if you want a query with several keys use compound index, use SON
from bson.son import SON
ordered_query = SON({'name': re.compile('^Miguel'), 'age':{'$lt': 200}})
res = dbconn.writers.find(ordered_query)
print list(res)


#==========================================================================================
#
#  Explain plans
#
#==========================================================================================


from pprint import pprint
pprint(dbconn.writers.find({"name": "Pablo Neruda"}).explain())


#==========================================================================================
#
#  Updating
#
#==========================================================================================

# Change the name of a field in a document
dbconn.writers.update({"name": "J. D. Salinger"}, {"name": "Jerome David Salinger"})

# if object does not exist, create new one (upsert)
dbconn.writers.update({"name": "George R. R. Martin"}, {"name": "George Raymond Richard Martin"}, upsert=True)

res = dbconn.writers.find_one({"name": "George Raymond Richard Martin"})
print res

#==========================================================================================
#
# dealing with subdocuments and arrays 
#
#==========================================================================================

# Add book as subdocument in collection
book = {'name': 'hobbit'}
dbconn.writers.update({"name": "Jerome David Salinger"},{'$set': {'books': book}})
dbconn.writers.update({"name": "George Raymond Richard Martin"},{'$set': {'books': {'name': 'another_book'}}})

# check the documents...
print dbconn.writers.find_one({"name": "Jerome David Salinger"})
print dbconn.writers.find_one({"name": "George Raymond Richard Martin"})

# Update subdocument field
dbconn.writers.update({"name": "George Raymond Richard Martin"},{'$set': {'books.name': 'lord_rings'}})
res = dbconn.writers.find_one({"name": "George Raymond Richard Martin"})
print res


# add one object to an array with push

edition = {
            'year': '1997',
            'editorial': 'planet'
        }
db_replica.books.update({'_id': 'hobbit' }, {'$push': {'editions': edition}}) # quite similar to mongo shell

print db_replica.books.find_one({'_id': 'hobbit'})

# try to perform array operation over non-array element
try:
    db_replica.books.update({'_id': 'lord_rings' }, {'$push': {'editions': edition}}) # non array operation
except OperationFailure as e:
    print e

# Create another edition
edition = {
            'year': '2001',
            'editorial': 'planet-lion'
        }
db_replica.books.update({'_id': 'hobbit' }, {'$push': {'editions': edition}})

# Result ..
for edition in db_replica.books.find_one({'_id': 'hobbit'})['editions']:
    print edition

# How to update one document name inside array of object ?:
db_replica.books.update(
            {'_id': 'hobbit', # find document hobbit
             'editions.year': '2001' # find subdocument inside editions array
            },
            {'$set': {'editions.$.editorial': 'planet-lion-updated'}} # work in subdocument of array
)

# Result
for edition in db_replica.books.find_one({'_id': 'hobbit'})['editions']:
    print edition


#==========================================================================================
#
# Dealing with Autoreconnect in replicaset
# Stop the mongo primary instance before continue
#==========================================================================================

import time
try:
    db_replica.books.find_one()
except AutoReconnect:
    print "Connection lost"

# We make same query again ...
print db_replica.books.find_one()

# as in the suggested rs config the 27017 has higher priority, would become primary again
# whe you restart the process


#===============================================================================
# SOURCES:
#  - http://api.mongodb.org/python/current/
#  - http://api.mongodb.org/python/current/examples/gevent.html
#  - http://api.mongodb.org/python/current/api/pymongo/collection.html
#  - http://api.mongodb.org/python/current/api/pymongo/connection.html
#===============================================================================

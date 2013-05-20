#-*- coding: utf-8 -*-
u"""
MOD: pymongo
"""


import pymongo


#===============================================================================
# 'pymongo' is the official Python MongoDB driver
#===============================================================================


# Let's connect to our database


client = pymongo.MongoClient('localhost', 27017)  # localhost:27017 is the default value
dbconn = client.mod_pymongo
# db.authenticate(username, password)  # Not enabled right now

dbconn.writers.drop()

#===============================================================================
# - When connecting you can provide a list of seeds (replica set servers) in several ways
#    - http://api.mongodb.org/python/current/examples/high_availability.html
#===============================================================================


#==========================================================================================
#
#  Inserting
#
#==========================================================================================


dbconn.writers.ensure_index([("name", pymongo.ASCENDING)], unique=True, name="unique_name")
dbconn.writers.insert({"name": "Jack London"})
dbconn.writers.insert({"name": "Honore de Balzac"})
dbconn.writers.insert({"name": "Lion Feuchtwanger"})  # Note that the collection is created on demand
dbconn.writers.insert({"name": "Emile Zola"})
dbconn.writers.insert({"name": "Truman Capote"})  # ObjectId (_id field value) is returned


# let's insert them using a list

more_writers = ["Yukio Mishima", "Lev Tolstoi", "Franz Kafka", "J. D. Salinger"]
for writer in more_writers:
    dbconn.writers.insert({"name": writer})


more_writers_using_bulk = ["Charles Bukowski", "Jorge Luis Borges", "Gabriel Garcia Marquez"]
dbconn.writers.insert([{"name": name} for name in more_writers_using_bulk])


#==========================================================================================
#
#  Querying
#
#==========================================================================================


cursor = dbconn.writers.find()
for writer in cursor:
    print writer


# query for an specific register
res = dbconn.writers.find_one({"name": "Pablo Neruda"})
print res

cursor = dbconn.writers.find({"name": "Pablo Neruda"})
for writer in cursor:
    print writer


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


dbconn.writers.update({"name": "J. D. Salinger"}, {"name": "Jerome David Salinger"})


dbconn.writers.update({"name": "George R. R. Martin"}, {"name": "George Raymond Richard Martin"}, upsert=True)

res = dbconn.writers.find_one({"name": "George Raymond Richard Martin"})
print res


#===============================================================================
# SOURCES:
#  - http://api.mongodb.org/python/current/
#  - http://api.mongodb.org/python/current/examples/gevent.html
#  - http://api.mongodb.org/python/current/api/pymongo/collection.html
#===============================================================================

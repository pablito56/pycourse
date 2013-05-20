#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD: Json handling
"""

import json  # Standard library provides a Json parser


# Let's initialize an encoded Json
encoded_json = """{
    "lk_location": {
        "long": 2.2205954,
        "lat": 41.4121694
    },
    "timestamp": "2013-02-22T12:21:05",
    "screen": true,
    "inst_apps": [
        "la.droid.qr",
        "com.shazam.android",
        "com.evernote",
        "com.eurosport",
        "com.whatsapp",
        "com.linkedin.android"
    ],
    "run_apps": [
        "com.android.chrome",
        "com.google.android.apps.translate",
        "com.google.android.apps.maps",
        "com.eurosport"
    ]
}"""


# Let's create some Python stuff
data = {"cloudcover": "25",
        "humidity": "88",
        "observation_time": "08:24 AM",
        "precipMM": "1.1",
        "pressure": "1018",
        "temp_C": "14",
        "temp_F": "57",
        "visibility": "10",
        "weatherCode": "116",
        "weatherDesc": [
                        {"value": "Partly Cloudy"}
                        ],
        "winddir16Point": "NNE",
        "winddirDegree": "20",
        "windspeedKmph": "11",
        "windspeedMiles": "7"
        }
data_list = [{"name": "Peter", "surname": "Parker", "alias": "Spiderman"},
             {"name": "Clrak", "surname": "Kent", "alias": "Superman"},
             {"name": "Tony", "surname": "Stark", "alias": "Ironman"},
             {"name": "Bruce", "surname": "Wayne", "alias": "Batman"}]


from pprint import pprint  # Bonus! pprint is a module for "pretty printing"


# Let's load (decode) the encoded Json
pprint(json.loads(encoded_json))


#===============================================================================
# Note how dates are decoded as a plain string. You must do the conversion "manually"
#===============================================================================


# Let's encode a Python dictionary
print repr(json.dumps(data))

print repr(json.dumps(data_list))


# You can tweak how data is encoded
print json.dumps(data, indent=4)  # Indent produces more human-readable output

# You can provide separators without spaces to produce more compact output
print repr(json.dumps(data_list, separators=(",", ":")))


#===============================================================================
# - Check all accepted parameters in the documentation
#    - Add custom parsers and handlers (for datetime...)
#
#    - Encode dates with custom handler:
#    http://blog.codevariety.com/2012/01/06/python-serializing-dates-datetime-datetime-into-json/
#
#    - Custom decoding with custom 'object_hook':
#    http://stackoverflow.com/questions/8793448/how-to-convert-to-a-python-datetime-object-with-json-loads
#
#    - Decode into OrderedDict using 'object_pairs_hook':
#    http://docs.python.org/2/library/json.html?highlight=json#json.load
#
# - Internally 'json.loads' and 'json.dumps' create a decoder or encoder instance
#    each time they are called, and this is not efficient
#===============================================================================


# Create the instance yourself to reuse it
decoder = json.JSONDecoder()
encoder = json.JSONEncoder()

pprint(decoder.decode(encoded_json))

print repr(encoder.encode(data))
print repr(encoder.encode(data_list))


# Let's try a 3rd party library
import simplejson


pprint(simplejson.loads(encoded_json))

print simplejson.dumps(data, indent=4)

print repr(simplejson.dumps(data_list, separators=(",", ":")))


#===============================================================================
# - 'simplejson' was included in Standard Library as 'json' in Python 2.6
# - It continues as an independent module for backwards compatibility
# - Their APIs are essentially the same, although there are minor differences
#    - 'simplejson.loads' and 'simplejson.dumps' internally create an instance too
# - simplejson has slightly better performance
#===============================================================================


# Let's try another 3rd party library
import ujson


pprint(ujson.loads(encoded_json))

print ujson.dumps(data)

print repr(ujson.dumps(data_list))  # Always compact output


#===============================================================================
# - 'ujson' is a pure C extension
# - It is several times faster than any other option
# - Its API is similar to json/simplejson interface, but more simple
#    - No encoder / decoder class (no internal instances)
#    - No indent or separator parameters
#    - Encodes datetime objects to seconds from epoch floats
#===============================================================================


#===========================================================================
# EXERCISE:
# - Execute the file 'exercises/mod_json/timeit_json.py':
#    $ python exercises/mod_json/timeit_json.py
#
# - Modify functions 'json_w_instance', 'simplejson_no_instance', 'simplejson_w_instance'
#    and 'ujson_no_instance' creating encoder / decoder instances and using different
#    Json libraries to enhance performance and let the asserts succeed
#===========================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/json.html?highlight=json#json
#  - http://pymotw.com/2/json/
#  - https://pypi.python.org/pypi/simplejson/3.3.0
#  - https://pypi.python.org/pypi/ujson
#  - http://www.justinfx.com/2012/07/25/python-2-7-3-serializer-speed-comparisons/
#===============================================================================

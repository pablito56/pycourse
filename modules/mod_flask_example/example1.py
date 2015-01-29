#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Mod: Flask example 1: basic api
"""

from flask import Flask


app = Flask(__name__)


# app is your Flask app declared above!
@app.route("/")
def root():
    return "Hello course attendees\n"  # This is the HTML response


#===========================================================================
# EXERCISE:
# - Execute the file "pycourse/modules/mod_flask_example/example1.py":
#    $ cd pycourse/modules/mod_flask_example
#    $ python example1.py
#
# - Retrieve the root index:
#    $ curl -i http://127.0.0.1:5000/
#
# - Modify function "root" to format the output HTML
#===========================================================================


if __name__ == "__main__":
    # Here we run the app
    app.run(debug=True)  # debug=True autoreloads code changes
    # DON'T USE THIS IN PRODUCTION!:
    #  - http://nichol.as/benchmark-of-python-web-servers
    #  - https://wiki.python.org/moin/WebServers

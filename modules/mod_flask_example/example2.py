#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Mod: Flask example 2: JSON, HTTP methods and error handling
"""

from flask import Flask, jsonify, request, abort, make_response


app = Flask(__name__)


@app.errorhandler(404)
def error_404(error):
    # This method is called each time the app is going to return a 404
    return make_response(jsonify({"code": "NOT_FOUND_URL", "msg": "The URL was not found"}), 404)


@app.route("/hello", methods=["GET"])
def get_hello():
    return jsonify({"hello": "Course attendees"})  # Voila! We return a JSON


@app.route("/hello", methods=["POST"])
def post_hello():
    if not request.json or "name" not in request.json:
        abort(400)
    print "INCOMING REQUEST:", request.json
    return jsonify({"hello": request.json["name"]}), 201  # This way we specify HTTP return code


#===========================================================================
# EXERCISE:
# - Execute the file "pycourse/modules/mod_flask_example/example2.py":
#    $ cd pycourse/modules/mod_flask_example
#    $ python example2.py
#
# - GET the hello JSON:
#    $ curl -i http://127.0.0.1:5000/hello
#
# - POST hello JSON:
#    $ curl -H "Content-Type: application/json" -d '{"name": "pablo"}' -i http://127.0.0.1:5000/hello
#
# - Modify functions "post_hello" and "get_hello" to save and return always the POST'ed name
#
# - Implement a command line client using requests and argparse
#
#===========================================================================


if __name__ == "__main__":
    app.run(debug=True)

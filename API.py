#
#  API.py
#  eAUrnik
#

import Timetable
from flask import Flask, request, make_response
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def page_not_found(e):
    return make_response("The request could not be processed. Check the provided information and try again.", 500)

class handle(Resource):
    def get(self, school, class_, student):
        timetable = Timetable.get(school, class_, student)
        response = make_response(timetable, 200)
        response.headers["content-type"] = "text/calendar"
        return response

api.add_resource(handle, "/urniki/<string:school>/razredi/<int:class_>/dijak/<int:student>")

if __name__ == "__main__":
    app.run(host = "::")

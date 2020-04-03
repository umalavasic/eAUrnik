
from flask import Flask, request, make_response
from flask_restful import Api, Resource, reqparse
from Handle import handle

app = Flask(__name__)
api = Api(app)

error_message = "The request could not be processed. Check the provided information and try again."
error_code = 500

@app.errorhandler(404)
def page_not_found(e):
    return make_response(error_message, error_code)

class handle_requested(Resource):
    def get(self, sola, razredi, dijak):
        data = handle(sola, razredi, dijak)
        if data is None:
            return make_response(error_message, error_code)
        response = make_response(data, 200)
        response.headers["content-type"] = "text/calendar"
        return response

api.add_resource(handle_requested, "/urniki/<string:sola>/razredi/<int:razredi>/dijak/<int:dijak>")

if __name__ == '__main__':
    app.run()

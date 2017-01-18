from flask import Flask, request, Request#, render_template, url_for, redirect, flash, session
from flask_restful import Api, Resource, fields, marshal_with
from random import randint

app = Flask(__name__)
api = Api(app)

request_fields = {"area_code": fields.Integer,
                 "lat": fields.Float,
                 "lng": fields.Float}

class Area_api(Resource):

    @marshal_with(request_fields)
    def get(self):
    	lat = request.values.get("lat")
    	lng = request.values.get("lng")
    	print lat, lng
        area_code = randint(0,9)
        output = {"area_code": area_code,
        		  "lat": lat,
        		  "lng": lng}
        return output, 200

    def post(self):
       pass

    def delete(self):
        pass

    def update(self):
        pass

api.add_resource(Area_api, '/api/v1/coord/')

if __name__ == "__main__":

    # seed here
    app.run(debug=True)
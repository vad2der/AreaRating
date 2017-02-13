from flask import Flask, request, Request, render_template#, url_for, redirect, flash, session
from flask_restful import Api, Resource, fields, marshal_with
from random import randint
import coord.coord as coord

app = Flask(__name__)
api = Api(app)

coord_fields = {"area_code": fields.Integer,
                 "lat": fields.Float,
                 "lng": fields.Float}

class Area_api(Resource):
    """
    class to process coordinate requests
    """
    @marshal_with(coord_fields)
    def get(self):
        lat = request.values.get("lat")
        lng = request.values.get("lng")        
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

@app.route('/')
def home():
    """
    initial info on the app to eleminate a confusion
    """
    return render_template('home.html')

if __name__ == "__main__":
    # seed here
    coord.create_tables()
    app.run(debug=True)
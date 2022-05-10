from flask import Flask, jsonify, request
from flask_cors import CORS

from flask import Flask
from handlers.add_country import add_new_country
from handlers.add_provinces import add_provinces
from handlers.create_tables import create_tables
from handlers.get_countries import fetch_countries
from handlers.get_country import fetch_country
from handlers.get_country_provinces import fetch_country_provinces


app = Flask(__name__)

CORS(app)

try:
    create_tables()

    @app.route("/")
    def hello():
        return "<p>Hello world, my first flask app</p>"

    # get country information
    @app.route('/country/<country>', methods=['GET'])
    def get_country(country):
        country = fetch_country(country)
        provinces = fetch_country_provinces(country['id'])

        return {"country": country, "provinces": provinces}

    # saves country and associated provinces data
    @app.route('/country', methods=['POST', 'GET'])
    def add_country():
        try:
            if request.method == 'POST':
                request_data = request.get_json()
                country = request_data['country']
                provinces = request_data['provinces']

                # saving country
                country_id = add_new_country(country)

                listOfProvinces = list()
                for province in provinces:
                    listOfProvinces.append((country_id, province['province'], province['confirmed'], province['deaths'],
                                            province['recovered'], province['updated']))

                # saving country provinces
                add_provinces(listOfProvinces)
                return {"message": "Country saved successfully", "success": True}
            else:
                # get saved countries
                countries = fetch_countries()
                return {
                    "countries": countries
                }
        except Exception as error:
            print("Failed adding country", error)
            return {"message": "Failed adding country", "success": False}
except:
    print("Failed creating tables")

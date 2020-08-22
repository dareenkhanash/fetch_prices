
import os

# Import the framework
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests
# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app, prefix="/api/v1")

@app.route("/")
def return_exchange_rate():
    return ("successfully")


class PrivateQuotes(Resource):
    def get(self):
        auth = request
        r =requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
                        '&from_currency=BTC&to_currency=USD&apikey=%s' % (os.environ.get('API_KEY')))

        return r.json()

    def post(self):
        return {'message': 'post'}

api.add_resource(PrivateQuotes, '/quotes')


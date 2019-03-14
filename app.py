import sys

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from classinator import BigfootClassinatorModel
from settings import Settings

app = Flask(__name__)


@app.route('/info', methods=['GET'])
@cross_origin()
def info():

  response = jsonify({
    'app'     : Settings.APP_NAME,
    'version' : Settings.APP_VERSION,
    'attribution' : Settings.APP_ATTRIBUTION
  })

  print(f"Response: {response.get_json()}")

  return response

@app.route('/classinate', methods=['POST'])
@cross_origin()
def classinate():

  print(f"Request: {request.get_json()}")

  sighting = request.get_json()['sighting']

  print(sighting)

  model = BigfootClassinatorModel()
  classination = model.classinate(sighting)

  response = jsonify(classination)

  print(f"Response: {response.get_json()}")

  return response

if __name__ == '__main__':
  app.run()

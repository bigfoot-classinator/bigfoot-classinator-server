import psycopg2

from datarobotai.client import DataRobotAIClient

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from settings import Settings
from data_access import DataAccess
from predictor import Predictor

# setup the object graph
settings = Settings()
data_access = DataAccess(settings)
predictor = Predictor(settings)

# create the flask application
app = Flask(__name__)


# /info route returns information about the application
@app.route('/info', methods=['GET'])
@cross_origin()
def info_route():
  return jsonify({
    'app'         : "Bigfoot Classinator",
    'version'     : "3.0.1",
    'attribution' : "AI by DataRobot"
  })


# /classinate route classinates a Bigfoot sighting
@app.route('/classinate', methods=['POST'])
@cross_origin()
def classinate_route():

  # get the sighting info from the request
  request_json = request.get_json()
  latitude = request_json['latitude']
  longitude = request_json['longitude']
  sighting = request_json['sighting']

  # prediction the class and then use it to predict the believability
  classination, class_a, class_b = predictor.classinate(sighting)
  believability = predictor.believify(latitude, longitude, sighting, classination)

  # if the believability is high enough, store it
  if believability >= settings.BELIEVABILITY_THRESHOLD:
    data_access.store_sighting(latitude, longitude, sighting, classination, believability)

  # return the prediction as JSON in the expected format
  return jsonify({
    'sighting' : sighting,
    'classination' : {
      'class_a'  : class_a,
      'class_b'  : class_b,
      'selected' : classination
    }
  })


# kick off the flask
if __name__ == '__main__':
  app.run()

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from classinator import BigfootClassinatorModel

app = Flask(__name__)

APP_NAME = "Bigfoot Classinator"
APP_VERSION = "0.0.1"

@app.route('/info', methods=['GET'])
@cross_origin()
def info():
  return jsonify({
    'app'     : APP_NAME,
    'version' : APP_VERSION
  })

@app.route('/classinate', methods=['POST'])
@cross_origin()
def classinate():
  sighting = request.get_json()['sighting']

  model = BigfootClassinatorModel()
  classination = model.classinate(sighting)

  return jsonify({
    'classination' : classination.to_dict(),
    'sighting'     : sighting
  })


if __name__ == '__main__':
  app.run()

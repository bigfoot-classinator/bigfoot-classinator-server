from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from classinator import BigfootClassinatorModel
from settings import Settings

app = Flask(__name__)


@app.route('/info', methods=['GET'])
@cross_origin()
def info():
  return jsonify({
    'app'     : Settings.APP_NAME,
    'version' : Settings.APP_VERSION
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

from datarobotai.client import DataRobotAIClient

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from settings import Settings

# create the flask application
app = Flask(__name__)

# get the DataRobot AI client and AI learning session
dr = DataRobotAIClient.create(username=Settings.USERNAME, key=Settings.API_KEY)
ai = dr.projects.get_project(Settings.PROJECT_ID)

# /info route returns information about the application
@app.route('/info', methods=['GET'])
@cross_origin()
def info():
  return jsonify({
    'app'     : Settings.APP_NAME,
    'version' : Settings.APP_VERSION,
    'attribution' : Settings.APP_ATTRIBUTION
  })

# /classinate route classinates a Bigfoot sighting
@app.route('/classinate', methods=['POST'])
@cross_origin()
def classinate():

  # get the sighting from the request
  request_json = request.get_json()
  sighting = request_json['sighting']

  # setup the prediction data
  # NOTE: ai.infer expects an array and can make multiple predictions
  # at once, but we only need one so we wrap it in an array
  data = [{ 'observed': sighting }]

  # infer the predictions and select the first one
  prediction = ai.infer('classification', data)[0]

  # return the prediction as JSON in the expected format
  return jsonify({
    'sighting' : sighting,
    'classination' : {
      'class_a'  : prediction.score_for("Class A"),
      'class_b'  : prediction.score_for("Class B"),
      'class_c'  : prediction.score_for("Class C"),
      'selected' : prediction.prediction
    }
  })

# kick off the flask
if __name__ == '__main__':
  app.run()

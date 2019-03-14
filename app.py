from datarobotai.client import DataRobotAIClient

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from settings import Settings

app = Flask(__name__)

dr = DataRobotAIClient.create(username=Settings.USERNAME, key=Settings.API_KEY)
ai = dr.projects.get_project(Settings.PROJECT_ID)

@app.route('/info', methods=['GET'])
@cross_origin()
def info():
  return jsonify({
    'app'     : Settings.APP_NAME,
    'version' : Settings.APP_VERSION,
    'attribution' : Settings.APP_ATTRIBUTION
  })

@app.route('/classinate', methods=['POST'])
@cross_origin()
def classinate():

  sighting = request.get_json()['sighting']

  predictions = ai.infer('classification', [{ 'observed': sighting }])
  p = predictions[0]

  return jsonify({
    'sighting' : sighting,
    'classination' : {
      'class_a'  : p.score_for("Class A"),
      'class_b'  : p.score_for("Class B"),
      'class_c'  : p.score_for("Class C"),
      'selected' : p.prediction
    }
  })

if __name__ == '__main__':
  app.run()

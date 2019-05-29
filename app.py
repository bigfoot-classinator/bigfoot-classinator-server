import os
import psycopg2

from datarobotai.client import DataRobotAIClient

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# create the flask application
app = Flask(__name__)

# get the API key and database URL from the environment
api_key = os.environ.get('DATAROBOTAI_API_KEY')
database_url = os.environ.get('DATABASE_URL')

# get the Project ID, SSL Mode, and Believability Threshold
# from the environment and log them

project_id = os.environ.get('BIGFOOT_CLASSINATOR_PROJECT_ID')
print('Project ID is', project_id)

ssl_mode = os.environ.get('SSL_MODE')
print('SSL Mode is', ssl_mode)

believability_threshold = os.environ.get('BELIEVABILITY_THRESHOLD')
try:
  float(believability_threshold)
except:
  believability_threshold = 0.0

print('Believability Threshold is', believability_threshold)

# create a DataRobot AI client
dr = DataRobotAIClient.create(api_key)

# load the project
ai = dr.projects.get(project_id)

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
  classination, class_a, class_b = classinate(sighting)
  believability = believify(latitude, longitude, sighting, classination)

  # if the believability is high enough, store it
  if believability >= believability_threshold:
    store_sighting(latitude, longitude, sighting, classination, believability)

  # return the prediction as JSON in the expected format
  return jsonify({
    'sighting' : sighting,
    'classination' : {
      'class_a'  : class_a,
      'class_b'  : class_b,
      'selected' : classination
    }
  })

def classinate(sighting):

  # setup the prediction data
  data = [{ 'observed': sighting }]

  # infer the predictions and select the first one
  prediction = list(ai.infer('classification', data))[0]

  # return the class and scores
  return prediction.prediction, prediction.score_for("Class A"), prediction.score_for("Class B")

def believify(latitude, longitude, sighting, classification):

  # setup the prediction data
  data = [{ 'latitude': latitude, 'longitude': longitude, 'observed': sighting, 'classification': classification }]

  # infer the predictions and select the first one
  prediction = list(ai.infer('believability', data))[0]

  # return the believability
  return prediction.prediction

def store_sighting(latitude, longitude, sighting, classination, believability):

  # get a connection to the database
  conn = psycopg2.connect(database_url, sslmode=ssl_mode)

  # get a cursor
  cur = conn.cursor()

  # if there isn't a table, create it
  cur.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' AND table_name='sightings';")
  count = cur.fetchone()[0]
  if count == 0:
    cur.execute("CREATE TABLE sightings (created_on timestamp, latitude decimal, longitude decimal, sighting text, classination varchar(7), believability decimal);")

  # insert the sighting
  cur.execute("INSERT INTO sightings (created_on, latitude, longitude, sighting, classination, believability) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s);", (latitude, longitude, sighting, classination, believability))

  # commit and close
  conn.commit()
  cur.close()
  conn.close()


# kick off the flask
if __name__ == '__main__':
  app.run()

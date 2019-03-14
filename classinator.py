from datarobotai.client import DataRobotAIClient
from settings import Settings

class BigfootClassinatorModel:
  def classinate(self, sighting):

    dr = DataRobotAIClient.create(username=Settings.USERNAME, key=Settings.API_KEY)
    ai = dr.projects.get_project(Settings.PROJECT_ID)

    predictions = ai.infer('classification', [{ 'observed': sighting }])
    p = predictions[0]

    return {
      'sighting' : sighting,
      'classination' : {
        'class_a'  : p.score_for("Class A"),
        'class_b'  : p.score_for("Class B"),
        'class_c'  : p.score_for("Class C"),
        'selected' : p.prediction
      }
    }

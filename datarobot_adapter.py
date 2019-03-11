from datarobotai.client import DataRobotAIClient
from settings import Settings

class DataRobotAdapter:
  def predict(self, data):
    dr = DataRobotAIClient.create(username=Settings.USERNAME, key=Settings.API_KEY)
    ai = dr.projects.get_project(Settings.PROJECT_ID)

    print(f"DataRobot Request Data: {data}")

    predictions = ai.infer('classification', data)

    return predictions[0]

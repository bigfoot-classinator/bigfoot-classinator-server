import requests

from settings import Settings

class DataRobotAdapter:
  def predict(self, data):
    url = Settings.DEPLOYMENT_URL
    auth = (Settings.USERNAME, Settings.API_TOKEN)
    headers = {
      'Content-Type': 'application/json; charset=UTF-8',
      'datarobot-key': Settings.DATAROBOT_KEY
    }

    print(f"DataRobot Request URL: {url}")
    print(f"DataRobot Request Data: {data}")

    response = requests.post(url, auth=auth, headers=headers, data=data)
    response_json = response.json()

    print(f"DataRobot Response: url={url} data={data}")

    return response_json

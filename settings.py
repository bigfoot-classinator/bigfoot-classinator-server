import os

class Settings:
  API_TOKEN = os.environ['DATAROBOT_API_KEY']
  USERNAME = os.environ['DATAROBOT_USERNAME']
  DATAROBOT_KEY = os.environ['DATAROBOT_KEY']
  DEPLOYMENT_ID = os.environ['BIGFOOT_DEPLOYMENT_ID']
  DEPLOYMENT_URL = 'https://datarobot-predictions.orm.datarobot.com/predApi/v1.0/deployments/%s/predictions' % DEPLOYMENT_ID

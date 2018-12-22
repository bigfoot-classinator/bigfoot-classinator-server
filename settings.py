import os

class Settings:
  APP_NAME = "Bigfoot Classinator"
  APP_VERSION = "2.1.0"

  API_TOKEN = os.environ['DATAROBOT_API_TOKEN']
  USERNAME = os.environ['DATAROBOT_API_USERNAME']
  DATAROBOT_KEY = os.environ['DATAROBOT_API_KEY']

  DEPLOYMENT_ID = os.environ['BIGFOOT_CLASSINATOR_DEPLOYMENT_ID']
  DEPLOYMENT_URL = 'https://datarobot-predictions.orm.datarobot.com/predApi/v1.0/deployments/%s/predictions' % DEPLOYMENT_ID

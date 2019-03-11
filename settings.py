import os

class Settings:
  APP_NAME = "Bigfoot Classinator"
  APP_VERSION = "3.0.0"
  APP_ATTRIBUTION = "AI by DataRobot"

  USERNAME = os.environ['AI_API_USERNAME']
  API_KEY = os.environ['AI_API_KEY']

  PROJECT_ID = os.environ['BIGFOOT_CLASSINATOR_PROJECT_ID']

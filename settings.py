import os

class Settings:

  def __init__(self):

    self.__api_key = os.environ.get('DATAROBOTAI_API_KEY')
    self.__project_id = os.environ.get('BIGFOOT_CLASSINATOR_PROJECT_ID')
    self.__database_url = os.environ.get('DATABASE_URL')
    self.__ssl_mode = os.environ.get('SSL_MODE')

    try:
      self.__threshold = float(os.environ.get('BELIEVABILITY_THRESHOLD'))
    except:
      self.__threshold = 0.0

    print("Project ID is", self.__project_id)
    print("SSL Mode is", self.__ssl_mode)
    print("Believability Threshold is", self.__threshold)

  @property
  def API_KEY(self):
    return self.__api_key

  @property
  def PROJECT_ID(self):
    return self.__project_id

  @property
  def DATABASE_URL(self):
    return self.__database_url

  @property
  def SSL_MODE(self):
    return self.__ssl_mode

  @property
  def BELIEVABILITY_THRESHOLD(self):
    return self.__threshold

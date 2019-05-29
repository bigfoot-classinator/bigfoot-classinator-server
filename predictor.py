from datarobotai.client import DataRobotAIClient

class Predictor:

  def __init__(self, settings):

    # create a DataRobot AI client
    dr = DataRobotAIClient.create(settings.API_KEY)

    # load the project
    self.__ai = dr.projects.get(settings.PROJECT_ID)

  def classinate(self, sighting):

    # setup the prediction data
    data = [{ 'observed': sighting }]

    # infer the predictions and select the first one
    prediction = list(self.__ai.infer('classification', data))[0]

    # return the class and scores
    return prediction.prediction, prediction.score_for("Class A"), prediction.score_for("Class B")

  def believify(self, latitude, longitude, sighting, classification):

    # setup the prediction data
    data = [{ 'latitude': latitude, 'longitude': longitude, 'observed': sighting, 'classification': classification }]

    # infer the predictions and select the first one
    prediction = list(self.__ai.infer('believability', data))[0]

    # return the believability
    return prediction.prediction

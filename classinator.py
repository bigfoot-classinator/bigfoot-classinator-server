import os
import json

from classination import BigfootClassination
from datarobot_adapter import DataRobotAdapter


class BigfootClassinatorModel:
  def classinate(self, sighting):
    data = [{ 'observed': sighting }]

    adapter = DataRobotAdapter()
    prediction = adapter.predict(data)

    return BigfootClassination.from_json(prediction)


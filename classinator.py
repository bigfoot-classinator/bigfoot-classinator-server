import os
import json

from pandas import DataFrame
from classination import BigfootClassination
from datarobot_adapter import DataRobotAdapter


class BigfootClassinatorModel:
  def classinate(self, sighting):
    data = DataFrame([{ 'observed': sighting }])
    data_json = data.to_json(orient='records')

    adapter = DataRobotAdapter()
    prediction = adapter.predict(data_json)

    return BigfootClassination.from_json(prediction)


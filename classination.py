class BigfootClassination:
  @classmethod
  def from_json(clazz, data):
    print(data['data'][0])
    classination = clazz()
    classination.__data = data['data'][0]
    return classination

  def to_dict(self):
    return {
      'class_a'  : self.class_a,
      'class_b'  : self.class_b,
      'class_c'  : self.class_c,
      'selected' : self.selected
    }

  @property
  def class_a(self):
    return self.__find('Class A')

  @property
  def class_b(self):
    return self.__find('Class B')

  @property
  def class_c(self):
    return self.__find('Class C')

  @property
  def selected(self):
    return self.__data['prediction']

  def __find(self, prediction_class):
    prediction_values = self.__data['predictionValues']
    prediction_value = next(value for value in prediction_values if value['label'] == prediction_class)
    return prediction_value['value']


# {
#   'data': [
#     {
#       'predictionValues':
#         [
#           {'value': 0.0057984682, 'label': 'Class C'},
#           {'value': 0.3942870124, 'label': 'Class B'},
#           {'value': 0.5999145194, 'label': 'Class A'}
#         ],
#       'prediction': 'Class A',
#       'rowId': 0
#     }
#   ]
# }
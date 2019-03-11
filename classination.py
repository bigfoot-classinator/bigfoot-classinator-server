class BigfootClassination:
  @classmethod
  def from_json(clazz, data):
    classination = clazz()
    classination.__data = data
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
    return self.__data.score_for('Class A')

  @property
  def class_b(self):
    return self.__data.score_for('Class B')

  @property
  def class_c(self):
    return self.__data.score_for('Class C')

  @property
  def selected(self):
    return self.__data.prediction

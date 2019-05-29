import psycopg2

class DataAccess:

  def __init__(self, settings):
    self.__url = settings.DATABASE_URL
    self.__ssl_mode = settings.SSL_MODE

  def store_sighting(self, latitude, longitude, sighting, classination, believability):

    # open the connection and get the cursor
    connection = psycopg2.connect(self.__url, sslmode=self.__ssl_mode)
    cursor = connection.cursor()

    # if there isn't a table, create it
    cursor.execute(SELECT_SIGHTINGS_TABLE_COUNT)
    if cursor.fetchone()[0] == 0:
      cursor.execute(CREATE_SIGHTINGS_TABLE)

    # insert the sighting
    cursor.execute(INSERT_SIGHTING, (latitude, longitude, sighting, classination, believability))

    # commit and close
    connection.commit()
    cursor.close()
    connection.close()


SELECT_SIGHTINGS_TABLE_COUNT = """
  SELECT
    count(*)
  FROM
    information_schema.tables
  WHERE
    table_schema='public' AND
    table_type='BASE TABLE' AND
    table_name='sightings';
"""

CREATE_SIGHTINGS_TABLE = """
  CREATE TABLE sightings (
    created_on timestamp,
    latitude decimal,
    longitude decimal,
    sighting text,
    classination varchar(7),
    believability decimal
  );
"""

INSERT_SIGHTING = """
  INSERT INTO sightings (
    created_on, latitude, longitude,
    sighting, classination, believability
  ) VALUES (
    CURRENT_TIMESTAMP, %s, %s, %s, %s, %s
  );
"""

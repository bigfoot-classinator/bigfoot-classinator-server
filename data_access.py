import psycopg2

class DataAccess:

  def __init__(self, settings):
    self.__url = settings.DATABASE_URL
    self.__ssl_mode = settings.SSL_MODE

  def store_sighting(self, latitude, longitude, sighting, classination, believability):

    # get a connection to the database
    conn = psycopg2.connect(self.__url, sslmode=self.__ssl_mode)

    # get a cursor
    cur = conn.cursor()

    # if there isn't a table, create it
    cur.execute("SELECT count(*) FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' AND table_name='sightings';")
    count = cur.fetchone()[0]
    if count == 0:
      cur.execute("CREATE TABLE sightings (created_on timestamp, latitude decimal, longitude decimal, sighting text, classination varchar(7), believability decimal);")

    # insert the sighting
    cur.execute("INSERT INTO sightings (created_on, latitude, longitude, sighting, classination, believability) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s, %s);", (latitude, longitude, sighting, classination, believability))

    # commit and close
    conn.commit()
    cur.close()
    conn.close()
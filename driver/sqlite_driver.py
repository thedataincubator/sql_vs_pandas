import os
import sqlite3
import pandas as pd # hack for loading

class SqliteDriver(object):
  def __init__(self, file, db):
    self.file = file
    self._db = db
    try:
      os.remove(self._db)
    except OSError:
      pass
    self._conn = sqlite3.connect(self._db)
    self._cursor = self._conn.cursor()

  def __del__(self):
    try:
      self._conn.close()
    except AttributeError:
      pass

  def load(self):
    self._cursor.execute('CREATE TABLE test (name varchar(255), dept char(1), birth int, salary double);')
    df = pd.read_csv(self.file)
    df.columns = ("name", "dept", "birth", "salary")
    df.to_sql('test', self._conn, flavor='sqlite', if_exists='replace')

  def groupby(self):
    self._cursor.execute('SELECT avg(birth), sum(salary) FROM test GROUP BY dept;')
    self._conn.commit()

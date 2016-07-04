import os
import sqlite3
import pandas as pd # hack for loading
from columns import bonus_columns, employee_columns

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
    df.columns = employee_columns
    df.to_sql('test', self._conn, flavor='sqlite', if_exists='replace')

  def groupby(self):
    self._cursor.execute('SELECT avg(birth), sum(salary) FROM test GROUP BY dept;')
    self._conn.commit()

  def filter(self):
    self._cursor.execute('SELECT * FROM test WHERE dept = "a";')
    self._conn.commit()

  def select(self):
    self._cursor.execute('SELECT name, dept FROM test')
    self._conn.commit()

  def sort(self):
    self._cursor.execute('SELECT * FROM test ORDER BY name ASC')
    self._conn.commit()

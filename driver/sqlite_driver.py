import os
import sqlite3
import pandas as pd # hack for loading
from columns import bonus_columns, employee_columns

class SqliteDriver(object):
  def __init__(self, employee_file, bonus_file, db):
    self.employee_file = employee_file
    self.bonus_file = bonus_file
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
    self._cursor.execute('CREATE TABLE employee (name varchar(255), dept char(1), birth int, salary double);')
    df = pd.read_csv(self.employee_file)
    df.columns = employee_columns
    df.to_sql('employee', self._conn, flavor='sqlite', if_exists='replace')

    self._cursor.execute('CREATE TABLE bonus (name varchar(255), bonus double);')
    df_bonus = pd.read_csv(self.bonus_file)
    df_bonus.columns = bonus_columns
    df_bonus.to_sql('bonus', self._conn, flavor='sqlite', if_exists='replace')

  def groupby(self):
    self._cursor.execute('SELECT avg(birth), sum(salary) FROM employee GROUP BY dept;')
    self._conn.commit()

  def filter(self):
    self._cursor.execute('SELECT * FROM employee WHERE dept = "a";')
    self._conn.commit()

  def select(self):
    self._cursor.execute('SELECT name, dept FROM employee;')
    self._conn.commit()

  def sort(self):
    self._cursor.execute('SELECT * FROM employee ORDER BY name ASC;')
    self._conn.commit()

  def join(self):
    self._cursor.execute('SELECT employee.name, employee.salary + bonus.bonus '
                         'FROM employee INNER JOIN bonus ON employee.name = bonus.name')
    self._conn.commit()

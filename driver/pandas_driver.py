import pandas as pd
import numpy as np
from columns import bonus_columns, employee_columns

class PandasDriver(object):
  def __init__(self, employee_file, bonus_file):
    self.employee_file = employee_file
    self.bonus_file = bonus_file

    self.df_employee = None
    self.df_bonus = None

  def load(self):
    self.df_employee = pd.read_csv(self.employee_file)
    self.df_employee.columns = employee_columns

    self.df_bonus = pd.read_csv(self.bonus_file)
    self.df_bonus.columns = bonus_columns

  def groupby(self):
    self.df_employee.groupby("dept").agg({'birth': np.mean, 'salary': np.sum})

  def filter(self):
    self.df_employee[self.df_employee['dept'] == 'a']

  def select(self):
    self.df_employee[["name", "dept"]]

  def sort(self):
    self.df_employee.sort_values(by='name')

  def join(self):
    joined = self.df_employee.merge(self.df_bonus, on='name')
    joined['total'] = joined['bonus'] + joined['salary']

import pandas as pd
import numpy as np
from columns import bonus_columns, employee_columns

class PandasDriver(object):
  def __init__(self, file):
    self.file = file
    self.df = None

  def load(self):
    self.df = pd.read_csv(self.file)
    self.df.columns = employee_columns

  def groupby(self):
    self.df.groupby("dept").agg({'birth': np.mean, 'salary': np.sum})

  def filter(self):
    self.df[self.df['dept'] == 'a']

  def select(self):
    self.df[["name", "dept"]]

  def sort(self):
    self.df.sort('name')

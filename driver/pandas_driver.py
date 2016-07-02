import pandas as pd
import numpy as np

class PandasDriver(object):
  def __init__(self, file):
    self.file = file
    self.df = None

  def load(self):
    self.df = pd.read_csv(self.file)
    self.df.columns = ("name", "dept", "birth", "salary")

  def groupby(self):
    self.df.groupby("dept").agg({'birth': np.mean, 'salary': np.sum})

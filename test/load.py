import pandas as pd
import numpy as np

df = pd.read_csv("data/sample.csv")
df.columns = ("name", "dept", "birth", "salary")

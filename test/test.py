import pandas as pd
import numpy as np
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Pandas operations')
  parser.add_argument('file', help='location of file')
  parser.add_argument('command', help='command to run')
  args = parser.parse_args()

  df = pd.read_csv(args.file)
  df.columns = ("name", "dept", "birth", "salary")

  if args.command:
    df.groupby("dept").agg({'birth': np.mean, 'salary': np.sum})

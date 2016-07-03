import argparse
import json
import sys

from contexttimer import Timer

from pandas_driver import PandasDriver
from sqlite_driver import SqliteDriver

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Pandas operations')
  parser.add_argument('file', help='location of csv data file')
  parser.add_argument('program', help='either pandas, sqlite, memory-sqlite')
  args = parser.parse_args()

  results = { 'program': args.program, 'file': args.file }

  if args.program == "pandas":
    driver = PandasDriver(args.file)
  elif args.program == "sqlite":
    driver = SqliteDriver(args.file, "data/test.db")
  elif args.program == "memory-sqlite":
    driver = SqliteDriver(args.file, ":memory:")
  else:
    raise ValueError("bad value for program")

  for task in ('load', 'groupby', 'filter', 'select', 'sort'):
    with Timer() as timer:
      getattr(driver, task)()
    results[task] = timer.elapsed

  json.dump(results, sys.stdout)
  print  # newline to file

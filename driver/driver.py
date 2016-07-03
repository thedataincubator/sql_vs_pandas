import argparse
import json
import sys

from contexttimer import Timer

from pandas_driver import PandasDriver
from sqlite_driver import SqliteDriver

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Pandas operations')
  parser.add_argument('file', help='location of csv data file')
  parser.add_argument('command', help='either pandas, sqlite, memory-sqlite')
  args = parser.parse_args()

  results = { 'command': args.command, 'file': args.file }

  if args.command == "pandas":
    driver = PandasDriver(args.file)
  elif args.command == "sqlite":
    driver = SqliteDriver(args.file, "data/test.db")
  elif args.command == "memory-sqlite":
    driver = SqliteDriver(args.file, ":memory:")
  else:
    raise ValueError("bad value for command")

  for task in ('load', 'groupby', 'filter', 'select'):
    with Timer() as timer:
      getattr(driver, task)()
    results[task] = timer.elapsed

  json.dump(results, sys.stdout)
  print  # newline to file

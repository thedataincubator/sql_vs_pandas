import argparse
import json
import sys

from contexttimer import Timer

from pandas_driver import PandasDriver
from sqlite_driver import SqliteDriver

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Pandas operations')
  parser.add_argument('n', help='size of files (for records only)')
  parser.add_argument('employee_file', help='location of employee csv data file')
  parser.add_argument('bonus_file', help='location of bonus_file csv data file')
  parser.add_argument('program', help='one of pandas, sqlite, or memory-sqlite')
  args = parser.parse_args()

  results = { 'program': args.program, 'n': args.n }

  if args.program == "pandas":
    driver = PandasDriver(args.employee_file, args.bonus_file)
  elif args.program == "sqlite":
    driver = SqliteDriver(args.employee_file, args.bonus_file, "data/test.db")
  elif args.program == "memory-sqlite":
    driver = SqliteDriver(args.employee_file, args.bonus_file, ":memory:")
  else:
    raise ValueError("bad value for program")

  for task in ('load', 'groupby', 'filter', 'select', 'sort', 'join'):
    with Timer() as timer:
      getattr(driver, task)()
    results[task] = timer.elapsed

  json.dump(results, sys.stdout)
  print  # newline to file

import random
import csv
import sys

if __name__ == "__main__":
  reader = csv.reader(sys.stdin)
  writer = csv.writer(sys.stdout)

  names = [row[0] for row in reader]
  random.shuffle(names)
  for name in names:
    writer.writerow((name, random.uniform(1e4, 1e5)))

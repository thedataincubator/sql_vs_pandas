import random
import string
import sys
import csv

def random_string(length, chars=string.ascii_letters):
  return ''.join(random.choice(chars) for _ in xrange(length))

def gen_csv(N):
  # ("Name", "Dept", "Birth", "Salary")
  for _ in xrange(N):
    yield (random_string(8), random_string(1, chars='abcdefg'), random.randint(1900, 2000), random.uniform(1e4, 1e5))

if __name__ == "__main__":
  length = int(sys.argv[1])
  with open(sys.argv[2], "w") as fh:
    writer = csv.writer(fh)

    for row in gen_csv(length):
      writer.writerow(row)

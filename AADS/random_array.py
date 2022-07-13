import random

def create_array(limit = 100, length = 20):
  rndNums = []

  for i in range(0, length):
    rndNums.append(random.randint(0, limit))

  return rndNums

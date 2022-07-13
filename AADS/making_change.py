from typing import List

def num_ways_for_change(amount: int, coins: List[int]) -> int:
  cache = [[0] * amount for i in range(len(coins))]
  for ci, cv in enumerate(coins):
    cache[ci][0] = 1

  for ci, cv in enumerate(coins):
    for a in range(1, amount):
      if coins[ci - 1] > a:
        cache[ci][a] = cache[ci - 1][a]
      else:
        cache[ci][a] = cache[ci - 1][a] + cache[ci][a - coins[ci - 1]]

  print(cache)
  return cache[-1][-1]

coins = [ 1, 5, 10, 25 ]
ways = num_ways_for_change(12, coins)
print(f'ways: {ways}')

from typing import List

class Chart:
  CORNERS = [-1, -1], [1, 1], [1, -1], [-1, 1]
  NESW = [0, -1], [1, 0], [0, 1], [-1, 0]
  DIRECTIONS = CORNERS + NESW

  def __init__(self, graph):
    self.graph = graph
    self.visited = [[False] * len(graph[0]) for i in range(len(graph))]
    self.islands = []

  def get_islands(self):
    return self.islands

  def define_island(self, x, y):
    self.set_visited(x, y)
    self.islands.append([[x, y]])
    self.traverse_island(x, y)

  def set_visited(self, x, y):
    self.visited[y][x] = True

  def traverse_island(self, x, y):
    for d in Chart.DIRECTIONS:
      dx = x + d[0]
      dy = y + d[1]

      # If index is out of bounds, or has already been visited, skip it
      if dx < 0 or dy < 0 or dy >= len(self.graph) or dx >= len(self.graph[0]) or self.visited[dy][dx]:
        continue

      self.set_visited(dx, dy)
      if self.graph[dy][dx]:
        self.islands[-1].append([dx, dy])
        self.traverse_island(dx, dy)

  def find_islands(self):
    for y, row in enumerate(self.graph):
      for x, value in enumerate(row):
        if value and not self.visited[y][x]:
          self.define_island(x, y)

  def get_island_graph(self):
    island_graph = [[0] * len(self.graph[0]) for i in range(len(self.graph))]
    for i, island in enumerate(self.islands):
      for [x, y] in island:
        island_graph[y][x] = i + 1

    return island_graph

  def get_largest_island(self):
    largest = []
    for island in self.islands:
      if (len(island) > len(largest)):
        largest = island

    return largest

def get_largest_island(grid: List[List[int]]) -> int:
  chart = Chart(grid)
  chart.find_islands()
  largest = chart.get_largest_island()
  return len(largest)

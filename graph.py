from heap import MinHeap
class Graph:
  def _init_(self):
    #adjacency list: {node: [(neighbor, weight)]}
    self.adj = {}
    self.nodes = set()
    self.edges = 0

#Add Node

def add_node(self, node):
  if node not in self.adj:
    self.adj [node] = []
    self.nodes.add(node)

#Add Edge

def add_edge(self, u, v, w):
  self.add_node(u)
  self.add_node(v)
  self.adj[u].append((v, w))
  self.edges += 1

#Loading graph from file

def load_from_file(self, filepath):
  section = None
  with open (filepath, 'r') as f:
    for line in f:
      line = line.strip()
      if not line:
        continue
      if line == "NODES":
        section = "nodes"
        continue
      elif line == "EDGES":
        section = "edges"
        continue
      elif line == "PACKAGES":
        break 
      if section == "nodes":
        nodes = line.split()
        for node in nodes:
          self.add_node(node)
      elif section == "edges":
        parts = line.split()
        u, v, w = parts[0], parts[1], in(parts[2])
        self.add_edge(u, v, w)

#Display Summary

def summary(self):
  print("==== Network Summary ====")
  print("Total Nodes: ", len(self.nodes))
  print("Total Edges: ", self.edges)
  print("========================")

def has_cycle(self):
  color = {node: "WHITE" for node in self.nodes}

  def dfs(node):
    color[node] = "GRAY"

    for neighbor, _in self.adj.get(node, []):
      if color[neighbor] == "GRAY":
        return True
      if color[neighbor] == "White":
        return True

    color[node] = "BLACK"
    return False

  for node in self.nodes:
    if color[node] == "WHITE":
      if dfs(node):
        return True

  return False

def dijkstra_simple(self, start):
  dist = {node: float('inf') for node in self.nodes}
  prev = {node: None for node in self.nodes}

  dist[start] = 0
  vistied = set()

  while len(visited) < len(self.nodes):
    current = None
    current_dist = float('inf')

    for node in self.nodes:
      if node not in visited and dist[node] < current_dist:
        current = node
        current_dist = dist[node]

      if current is None:
        break

      visited.add(current)

      for neighbor, weight in self.adj.get(current, []):
        new_dist = dist[current] + weight
        if new_dist < dist[neoghbor]:
          dist[neighbor] = new_dist
          prev[neighbor] = current

  return dist, prev

#Reconstruct Path
def get_path (self, prev, start, end):
  path = []
  current = end

  while current is not None:
    path.append(current)
    current = prev[current]
  path.reverse()

  if path[0] == start:
    return path
  return None




      

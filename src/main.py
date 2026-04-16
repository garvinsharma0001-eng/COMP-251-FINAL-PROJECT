from graph import Graph
from utils import Package, DispatchQueue
from hashmap import HashMap
from trie import Trie

def load_packages(filepath):
  queue = DispatachQueue()
  section = None

  with open(filepath, 'r') as f:
    for line in f:
      line = line.strip()

      if line == "PACKAGES":
        section = "packages"
        continue

      if section == "packages" and line:
        parts = line.split()
        pkg_id = parts[0]
        priority = int(parts[1])
        destination = parts[2]
        weight = float(parts[3])

        package = Package(pkg_id, priority, destination, weight)
        queue.enqueue(package)

return queue

# Build Depot HashMap
def build_depot_map(graph):
  depot_map = HashMap()

  for node in graph. nodes:
    data = {
      "location": "Unknown",
      "capactiy": 100,
      "active": True
    }
    depot_map.insert(node, data)
  return deport_map

#Build Trie
def build_trie(graph):
  trie = Trie()

  for node in graph.nodes:
    trie.insert(node)
  return trie

# Main 
def main():
  graph = Graph()
  graph.load_from_file("../data/network.txt")

  desipatch_queue = load_packages("../data/network.txt")

  while True:
    print("\n======Smart Network Logistixs Engine========")
    print("1. Display Network Summary")
    print("2. Find Shortest Path")
    print("3. Detect Cycles")
    print("4. Dispatch Highest-Priority Package")
    print("5. Exit")
    print("===========================================")

    choice = input ("Enter choice: ")

    if choice == "1":
      graph.summary()
    elif choice == "2":
      start = input("Enter source: ")
      end = input("Enter destination: ")

      cost, path = graph.dijkstra(start, end)

      if path:
        print("Shortest Path: ", "->". join(path))
        print("Total Cost: ", cost)
      else:
        print("No path found")

    elif choice == "3":
      if graph.has_cycle():
        print("Cycle detected in the network.")
      else:
        print("No cycles found.")

    elif choice == "4":
      package = dispatch_queue.dequeue()
      if package:
        print("Disptached: ", package)

    elif choice == "5":
      print("Exiting....")
      break

    else:
      print("Invalid choice. Try again")

if _name_ == "_main_":
  main()

    
      
      

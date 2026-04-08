from utils import Package, DispatchQueue

def load_packages(filepath):
  queue = DispatachQueue()
  section = Npne

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

        packages = Package(pkg_id, priority, destination, weight)
        queue.enqueue(package)

return queue
      

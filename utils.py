from heap import MaxHeap

class Package:
  def _init_(self, package_id, priority, destination, weight):
    self.package_id = package_id
    self.priority = priority
    self.destination = destination
    self.weight = weight

  def _repr_(self):
    return f"{self.package_id} (Priority: {self.priority}, Dest: {self.destination}, Weight: {self.weight}kg)"

class DispatachQueue:
  def _init_(self):
    self.heap = MaxHeap()

# Add package
def enqueue(self, package):
  #store as (priority, package)
  self.heap.push((package.priority, package))

# Remove highest priority
def dequeue (self):
  if self.heap.is_empty():
    print("No packages to dispatch.")
    return None

  priority, package = self.heap.pop()
  return package

def peek(self):
  if self.heap.is_empty():
    return None
  return self.heap.peek()[1]

def is_empty(self):
  return self.heap.is_empty()

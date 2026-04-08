class MinHeap: 
  def _init_(self):
    self.data = []

#Helper functions

def _parent(self, i):
  return (i - 1) // 2

def _left(self, i):
  return 2 * i + 1

def _right(self, i):
  return 2 * i + 2

def _swap(self, i, j):
  self.data[i], self.data[j] = self.data[j], self.data[i]

# Insert push

def push(self, item):
  self.data.append(item)
  self._healpify_up(len(self.data) - 1)

def _heapify_up(self, i):
  while i > 0 and self.data[i][0] < self.data[self._parent(i)][0]:
    self._swap(i, self._parent(i))
    i = self._parent(i)


#Remove smallest (pop)

def pop(self):
  if not self.data:
    return None
  if len(self.data) == 1:
    return self.data.pop()

  root = self.data[0]
  self.data[0] = self.data.pop()
  self._heapify_down(0)

  return root

def _heapify_down(self, i):
  smallest = i
  left = self._left(i)
  right = self._right(i)

  if left < len(self.data) and self.data[left][0] < self.data[smallest][0]:
    smallest = left
  if right < len(self.data) and self.data[right][0] < self.data[smallest][0]:
    smallest = right

  if smallest != i:
    self._swap(i, smallest)
    self._heapify_down(smallest)

def is_empty(self):
  return len(self.data) == 0


class MaxHeap:
  def _init_(self):
    self.data = []

  def _parent(self, i):
    return (i - 1) // 2

  def _left(self, i):
    return 2 * i + 1

  def _right(self, i):
    return 2 * i + 2

  def _swap(self, i ,j):
    self.data[i], self.data[j] = self.data[j], self.data[i]

# Insert
def push (self, item):
  self.data.append(item)
  self._heapify_up(len(self.data) - 1)

def _heapify_up(self, i):
  while i>0 and self.data[i][0] > self.data[self._parent(i)[0]]:
    self._swap(i, self._paretn(i))
    i = self._parent(i)

# Remove max
def pop(self):
  if not self.data:
    return None

  if len(self.data) == 1:
    return self.data.pop()

  root = self.data[0]
  self.data[0] = self.data.pop()
  self._heapify_down(0)

  return root

def _heapify_down(self, i):
  largest = i
  left = self._left(i)
  right = self._right(i)

  if left < len(self.data) and self.data[left][0] > self.data[largest][0]:
    largest = left

  if right < len(self.data) and self.data[right][0] > self.data[largest][0]:
    largest = right

  if largest != i:
    self._swap(i, largest)
    self._heapify_down(largest)


def peek(self):
  return self.data[0] if self.data else None

def is_empty (self):
  return len(self.data) == 0

    
    
  

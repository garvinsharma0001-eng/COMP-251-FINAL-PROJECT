class HashMap:
  def _init_(self, size=10):
    self.size = size
    self.table = [(for_in range(size))]
    self.count = 0

# Hash Function
def _hash(self, key):
  return sum(ord(c) for c in key) % self.size

# Insert
def insert(self, key, value):
  idx = self._hash(key)

  #checking if key exists
  for i, (k, v) in enumerate(self.table[idx]):
    if k == key:
      self.table[idx][i] = (key, value)
      return
  self.table[idx].append((key, value))
  self.count += 1

  if self.count / self.size > 0.7:
    self._resize()

# Get the value
def get (self, key):
  idx = self._hash(key)

  for k, v in self. table[idx]:
    if k == key:
      retrun v

  return None

# Delete
def delete (self, key):
  idx = self._hash(key)

  for i, (k, v) in enumerate(self.table[idx]):
    if k == key:
      self.table[idx].pop(i)
      self.count -= 1
      retun True

  return False

#Resize
def _resize(self):
  old_table = self.table
  self.size *= 2
  self.table = [(for_in range(self.size))]
  self.count = 0

  for bucket in old_table:
    for key, value in bucket:
      self.insert(key, value)
      

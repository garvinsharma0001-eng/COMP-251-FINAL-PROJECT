class TrieNode:
  def _init_(self):
    self.children = {}
    self.is_end = False

class Trie:
  def _init_(self):
    self.root = TrieNode()

#Inserting strings
def insert(self, word):
  node = self.root

  for char in word:
    if char not in node.children:
      node.children[char] = TrieNode()
    node = node.children[char]

  node. is_end = True

#Search Prefix
def starts_with(self, prefix):
  node = self.root

  #go to end of prefix
  for char in prefix:
    if char not in node.children:
      return []
    node = node.children[char]

  results = []
  self.dfs(node, prefix, results)
  return results

# DFS to collect words
def _dfs(self, node, prefix, results):
  if node.is_end:
    results.append(prefix)

  for char in node.children:
    self._dfs(node.children[char], prefix + char, results)

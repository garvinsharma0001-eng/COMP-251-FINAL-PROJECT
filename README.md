# COMP-251-FINAL-PROJECT
Smart Network Logistics Engine
Name: Garvin Sharma
Student ID: 300213059

How to run: python src/main.py

This project implements a SNLE using core data structures and algorithms. The system models a city delivery network as a directed weighted graph and supports routing, cycle detection, package dispatching and search features.

There are various features included in this project:
1.) Graphs create adjacency list representation. Also, they load network.txt from file provided. Supports directed weighted edges.
2.) Dijkstra's Algorithm: this algorithm is implememnted using a custom MinHeap. The algoritham helps finding shortest path between nodes.
3.) DFS with node coloring helps in cycle detection.
4.) Priority Dispatch Queue (heap.py): MaxHeap Implementation. This dispatches highest priority package first.
5.) Hash Map: Supports custom implementation using chaining algorithm. Supports inser, search, delete and resize.
6.) Trie.py : Supports prefix-based search.

File Structure:
graph.py --> Graph + Algorithams.
heal.py --> MinHeap and MaxHeap
hashmap.py --> Custorm hash map
trie.py --> Autocomplete system
utils.py --> Package + DispatchQueue
main.py --> CLI interface

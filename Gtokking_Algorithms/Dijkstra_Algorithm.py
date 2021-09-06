# Graph Hash Table
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
print(graph["start"].keys())  # start Neighbors
graph["a"] = {}
graph["a"]["fin"] = 1
print(graph["a"].keys())  # a Neighbors
graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3
print(graph["b"].keys())  # b Neighbors

# Cost Hash Table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents Hash Table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None




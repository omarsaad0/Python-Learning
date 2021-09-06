# Graph Hash Table
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
#print(graph["start"].keys())  # start Neighbors
graph["a"] = {}
graph["a"]["fin"] = 1
#print(graph["a"].keys())  # a Neighbors
graph["b"] = {}
graph["b"]["fin"] = 5
graph["b"]["a"] = 3
graph["fin"] = {}
#print(graph["b"].keys())  # b Neighbors

# Cost Hash Table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
#print(costs)
# Parents Hash Table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []
route = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_fastest_path():
    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


def display_route(node=None):

    start_node = 'start'  # we look for this 'value'
    end_node = 'fin'  # we look for this 'key'

    if node == start_node:  # we're done
        route.append(node)
        reverse_route = list(reversed(route))
        print('Fastest Route: ' + ' -> '.join(reverse_route))

    elif node is None:  # begin processing (this condition only passes once)
        end_parent = parents[end_node]  # get the parent node for the end node
        route.append(end_node)
        display_route(end_parent)

    else:
        parent = parents[node]
        route.append(node)
        display_route(parent)

find_fastest_path()
display_route()
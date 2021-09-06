from collections import deque

graph = {}
graph["You"] = ["Bob", "Clair", "Alice"]
graph["Bob"] = ["Anuj", "Peggye"]
graph["Clair"] = ["Thom", "Jonny"]
graph["Alice"] = ["Peggye"]
graph["Anuj"] = []
graph["Thom"] = []
graph["Peggye"] = []
graph["Jonny"] = []


def person_is_seller(name):
    return name[-1] == 'e'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " Is a Mango Seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("You")
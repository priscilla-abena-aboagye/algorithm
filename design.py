copper = {
    "species": "guinea pig",
    "age": 16,
    "food": "hay"
}

copper["species"] = "Cavia porcellus"

del copper["age"]

for i, j in copper.items():
    print(i, j)

my_graph = {
    "A": [("B", 3), ("D", 1)],
    "B": [("A", 3), ("C", 4)],
    "C": [("B", 4), ("D", 7)],
    "D": [("A", 1), ("C", 7)]
}

def shortest_path(graph, start):
    unvisited = []
    for i in unvisited:
        unvisited.append(i)
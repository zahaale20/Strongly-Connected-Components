# CSC 349
# Lab 2: Strongly Connected Components
# Alex Zaharia

import sys
import math


class node:
    def __init__(self, name, out_edges, in_edges, previsit=-1, postvisit=-1, component=None):
        self.name = name
        self.out_edges = out_edges
        self.in_edges = in_edges
        self.previsit = previsit
        self.postvisit = postvisit
        self.component = component


def strong_connectivity(G):
    stack = []
    component_list = []

    for i in range(len(G)):
        if not G[i].previsit:
            visitVertex(G, G[i], stack)

    while stack:
        vertex = stack.pop()
        if not vertex.postvisit:
            new = []
            c = assignToComponent(G, vertex, new)
            component_list.append(c)

    sort_component_list(component_list)
    return component_list


def sort_component_list(components):
    for c in components:
        c.sort()
    components.sort(key=lambda x: x[0])


def read_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        v = int(lines[0])
        if v == 0:
            raise ValueError("Graph must have one or more vertices")

        G = [node(name=i, out_edges=[], in_edges=[], previsit=False, postvisit=False, component=None) for i in range(v)]
        for line in lines[1:]:
            fromVertex, toVertex = map(int, line.strip().split(","))
            G[fromVertex].out_edges.append(toVertex)
            G[toVertex].in_edges.append(fromVertex)

    return G


def visitVertex(graph, vertex, stack):
    vertex.previsit = True
    neighbors = vertex.out_edges
    for i in range(len(neighbors)):
        neighbor = neighbors[i]
        if not graph[neighbor].previsit:
            visitVertex(graph, graph[neighbor], stack)
            neighbors = vertex.out_edges
            i = 0
    stack.append(vertex)


def assignToComponent(graph, vertex, component_list):
    vertex.postvisit = True
    component_list.append(vertex.name)
    neighbors = vertex.in_edges
    for i in range(len(neighbors)):
        if not graph[neighbors[i]].postvisit:
            assignToComponent(graph, graph[neighbors[i]], component_list)
    return component_list


def main():
    filename = sys.arv[1]
    # filename = "lab2_example1"
    G = read_file(filename)
    components = strong_connectivity(G)
    print(components)


if __name__ == '__main__':
    main()

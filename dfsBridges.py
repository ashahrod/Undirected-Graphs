from os import read
import sys
from collections import defaultdict

class Graph:
  
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.numVertices = vertices
        self.visitNum = 0
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def findBridge(self):
        visited = (self.numVertices) * [False]
        visit_nums = [float("inf")] * (self.numVertices)
        low = [float("inf")] * (self.numVertices)
        parent = (self.numVertices) * [-1] 
        for i in range(self.numVertices):
            if visited[i] == False:
                self.helperBridge(i, visited, visit_nums, parent, low)

    #  notes: u is the next vertex, visited[] contains the visited vertices
    #  visit_nums[] contains the visit nums, low[] contains the low visit nums, parent[] contains the parent vertices
    def helperBridge(self,u, visited, visit_nums, parent, low):
 
        # Mark the current node as visited
        visited[u]= True
 
        visit_nums[u] = self.visitNum
        low[u] = self.visitNum
        self.visitNum += 1
 
        for vertice in self.graph[u]:
            if visited[vertice] == False :
                parent[vertice] = u
                self.helperBridge(vertice, visited, visit_nums, parent, low)
                low[u] = min(low[u], low[vertice])

                if visit_nums[u] < low[vertice]:
                    bridges.append([u, vertice])

            elif vertice != parent[u]:
                low[u] = min(low[u], visit_nums[vertice])
# GLOBAL
bridges = []


def read_file(file_name):
    f = open(file_name, 'r')
    edges = [] 
    seen = []
    for line in f.readlines():
    #need to make the strings ints
        # print(line)
        mapped = map(int, line.split(", "))
        temp_list = list(mapped)
        edges.append(temp_list)
        if temp_list[0] not in seen:
            seen.append(temp_list[0])
        if temp_list[1] not in seen:
            seen.append(temp_list[1])

    # print(edges)
    # print(seen)
    # print(len(seen))
    return edges, len(seen)

def makeGraph(edges, numVertices):
    graph = Graph(numVertices)
    for edge in edges:
        graph.addEdge(edge[0], edge[1])
    return graph

def print_out():
    for bridge in bridges:
        bridge.sort()
    sorted_list = sorted(bridges, key=lambda x: (x[0], x[1]))
    if sorted_list:
        print("Contains %d bridge(s):" %len(sorted_list))
        for bridge in sorted_list:
            print(str(bridge[0]) + ", " + str(bridge[1]))
    else:
        print("Contains no bridges.")


def main():
    edges, num_vertices = read_file(sys.argv[1])
    graph = makeGraph(edges, num_vertices)
    graph.findBridge()
    print_out()

main()
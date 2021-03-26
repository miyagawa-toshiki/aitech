import sys
class Graph():

    def __init__(self, vertex):
        self.V = vertex
        self.graph = [[0 for column in range(vertex)]for row in range(vertex)]

    def printSolution(self, dist):
        print("Vertex distance from source")
        for node in range(self.V):
            print(node, " ", dist[node])
    
    def minDistance(self, dist, spots):

        #Initilaize minimum distance for next node
        min = sys.maxsize

        #Search not nearest vertex not in the shortest path tree
        for v in range(self.V):
            if dist[v] < min and spots[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    
    def dijekstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spots = [False] * self.V

        for cont in range(self.V):

            u = self.minDistance(dist, spots)

            spots[u] = True

            for v in range(self.V):
                if self.graph[u] [v] > 0 and spots[v] == False and dist[v] > dist[u] + self.graph[u] [v]:
                    dist[v] = dist[u] + self.graph[u] [v]
            
        self.printSolution(dist)

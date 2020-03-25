# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 


INF = 1000000


class CGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices] * vertices
        self.dist = 0
        self.prev = [0] * vertices

    def print_solution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree 
    def min_distance(self, dist, sptSet):
        # Initilaize minimum distance for next node 
        min = INF
        min_index = 0

        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index
        # Funtion that implements Dijkstra's single source

    # shortest path algorithm for a graph represented
    # using adjacency matrix representation 
    def dijkstra(self, src):
        self.dist = [INF] * self.V
        self.dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.min_distance(self.dist, sptSet)

            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True

            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] is False and \
                        self.dist[v] > self.dist[u] + self.graph[u][v]:
                    self.dist[v] = self.dist[u] + self.graph[u][v]
                    self.prev[v] = u


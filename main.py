from Graph import CGraph
from sys import maxsize

file = open('easy_01_tsp.txt', 'r')

nCities = int(file.readline())
graph = CGraph(nCities)
g_input = []


for i in range(0, nCities):
    line = file.readline().strip('\n')
    distances = [int(x) for x in line.split(',')]
    g_input.append(distances)
    graph.graph[i] = distances

start = int(file.readline()) - 1
finnish = int(file.readline()) - 1

# ==============================================
# ==============================================
# ==============================================
from sys import maxsize

V = nCities


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:
        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path


# next_permutation implementation
def next_permutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


# matrix representation of graph
Groaf = g_input
s = start
print(nCities)
print("1 2 3 4 etc")
print(travellingSalesmanProblem(Groaf, s))
# ==============================================
# ==============================================
# ==============================================


graph.dijkstra(start)

dist = graph.dist[finnish]
path = []
while finnish is not start:
    path.append(finnish)
    finnish = graph.prev[finnish]

path.append(start)

path.reverse()

print(len(path))
for i in range(0, len(path)):
    print(path[i] + 1, end=' ')
print()
print(dist)

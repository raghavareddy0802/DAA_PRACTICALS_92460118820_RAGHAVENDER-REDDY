from itertools import permutations

def tsp(graph, n):
    start = 0
    vertices = []

    for i in range(n):
        if i != start:
            vertices.append(i)

    min_cost = float('inf')
    best_path = []

    for path in permutations(vertices):
        current_cost = 0
        k = start

        for j in path:
            current_cost += graph[k][j]
            k = j

        current_cost += graph[k][start]

        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [start] + list(path) + [start]

    print("\nMinimum Cost Tour:")

    for vertex in best_path:
        print(vertex + 1, end=" ")

    print("\nMinimum Cost:", min_cost)


n = int(input("Enter number of cities: "))

graph = []

print("Enter cost adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

tsp(graph, n)
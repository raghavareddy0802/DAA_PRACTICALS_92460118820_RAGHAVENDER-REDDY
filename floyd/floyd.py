def floyd(graph, n):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    print("\nShortest Distance Matrix:")

    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix (use 999 for no edge):")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append([
        float('inf') if x == 999 else x for x in row
    ])

floyd(graph, n)
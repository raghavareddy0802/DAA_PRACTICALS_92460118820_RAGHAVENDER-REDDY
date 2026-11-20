def prim(graph, start, n):

    visited = [False] * n
    visited[start] = True

    total_cost = 0

    print("Edges in Minimum Spanning Tree:")

    for _ in range(n - 1):

        minimum = float('inf')
        x = -1
        y = -1

        for i in range(n):

            if visited[i]:

                for j in range(n):

                    if not visited[j] and graph[i][j] != 0:

                        if graph[i][j] < minimum:

                            minimum = graph[i][j]
                            x = i
                            y = j

        if x == -1:
            print("Graph is disconnected. MST cannot be formed.")
            return

        print(x + 1, "-", y + 1, ":", minimum)

        total_cost += minimum
        visited[y] = True

    print("Minimum cost:", total_cost)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertex: "))
start = start - 1

prim(graph, start, n)
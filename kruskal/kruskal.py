
def find(parent, vertex):

    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])

    return parent[vertex]


def union(parent, rank, u, v):

    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


def kruskal(graph, n):

    edges = []

    for i in range(n):
        for j in range(i + 1, n):

            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()

    parent = [i for i in range(n)]
    rank = [0] * n

    total_cost = 0
    count = 0

    print("Edges in Minimum Spanning Tree:")

    for weight, u, v in edges:

        if union(parent, rank, u, v):

            print(u + 1, "-", v + 1, ":", weight)

            total_cost += weight
            count += 1

            if count == n - 1:
                break

    if count != n - 1:
        print("Graph is disconnected. MST cannot be formed.")
    else:
        print("Minimum cost:", total_cost)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

kruskal(graph, n)
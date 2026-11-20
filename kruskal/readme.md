# Kruskal's Algorithm

## Aim
To implement Kruskal's Algorithm to find the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph using Python.

## Theory

Kruskal's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, weighted graph.

A Minimum Spanning Tree is a subset of edges that:
- Connects all vertices in the graph.
- Contains exactly V - 1 edges, where V is the number of vertices.
- Does not contain any cycles.
- Has the minimum possible total edge weight.

Kruskal's Algorithm selects edges in increasing order of their weights. An edge is added to the MST only if it does not form a cycle.

## Algorithm

1. Start with an empty list of edges.
2. Extract all edges from the adjacency matrix.
3. Sort the edges in ascending order of their weights.
4. Initialize each vertex as a separate set.
5. Select the edge with the minimum weight.
6. Check whether the selected edge forms a cycle using the Union-Find operation.
7. If it does not form a cycle, add the edge to the MST.
8. Repeat until V - 1 edges have been selected.
9. Calculate and display the total minimum cost.

## Python Program

\```python
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
\```

## Sample Input

\```text
Enter number of vertices: 4

Enter adjacency matrix:
0 2 4 6
2 0 0 3
4 0 0 5
6 3 5 0
\```

## Sample Output

\```text
Edges in Minimum Spanning Tree:
1 - 2 : 2
2 - 4 : 3
1 - 3 : 4
Minimum cost: 9
\```

## Explanation

The given graph contains four vertices and the following weighted edges:

| Edge | Weight |
|------|--------|
| 1 - 2 | 2 |
| 1 - 3 | 4 |
| 1 - 4 | 6 |
| 2 - 4 | 3 |
| 3 - 4 | 5 |

Kruskal's Algorithm sorts all edges in ascending order of weight:

1. Select edge (1, 2) with weight 2.
2. Select edge (2, 4) with weight 3.
3. Select edge (1, 3) with weight 4.

All four vertices are connected using three edges. Since the number of selected edges is V - 1, the algorithm terminates.

**Minimum Spanning Tree Cost = 2 + 3 + 4 = 9**

## Important Functions

### 1. find()

The find() function identifies the representative or root of the set containing a vertex. It uses path compression to make future searches faster.

### 2. union()

The union() function combines two different sets. It uses union by rank to keep the tree structure efficient. If both vertices already belong to the same set, adding the edge would create a cycle.

### 3. Edge Sorting

The edges are sorted in ascending order using:

\```python
edges.sort()
\```

This ensures that the algorithm considers the smallest-weight edges first.

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Extracting edges from adjacency matrix | O(V²) |
| Sorting edges | O(E log E) |
| Union-Find operations | O(E α(V)) |
| Overall | O(V² + E log E) |

Here:
- V = Number of vertices
- E = Number of edges
- α(V) = Inverse Ackermann function, which grows extremely slowly.

## Space Complexity

- Adjacency matrix: O(V²)
- Edge list: O(E)
- Parent and rank arrays: O(V)

Auxiliary space complexity: **O(E + V)**.

## Advantages

- Simple and efficient greedy algorithm.
- Finds a Minimum Spanning Tree.
- Avoids cycles using the Union-Find data structure.
- Works well for sparse graphs.

## Applications

- Designing computer networks.
- Road and railway network planning.
- Electrical power distribution.
- Network cable optimization.
- Connecting multiple locations with minimum cost.


## Result

Thus, Kruskal's Algorithm was successfully implemented in Python to find the Minimum Spanning Tree of a weighted, undirected graph, and the minimum cost was calculated.
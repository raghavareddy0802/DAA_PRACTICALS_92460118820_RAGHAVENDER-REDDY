# Prim's Algorithm

## Aim

To implement Prim's Algorithm to find the Minimum Spanning Tree (MST) of a connected, undirected, weighted graph using Python.

## Theory

Prim's Algorithm is a greedy algorithm used to find the Minimum Spanning Tree of a connected, undirected, weighted graph.

A Minimum Spanning Tree is a subset of edges that:

- Connects all vertices in the graph.
- Contains exactly V - 1 edges, where V is the number of vertices.
- Does not contain any cycles.
- Has the minimum possible total edge weight.

Prim's Algorithm starts from a selected vertex and gradually grows the Minimum Spanning Tree by selecting the minimum-weight edge that connects a visited vertex to an unvisited vertex.

The process continues until all vertices are included in the MST.

## Algorithm

1. Start with a weighted, undirected graph represented using an adjacency matrix.
2. Read the number of vertices and the starting vertex.
3. Initialize all vertices as unvisited.
4. Mark the starting vertex as visited.
5. Find the minimum-weight edge connecting a visited vertex to an unvisited vertex.
6. Add the selected edge to the Minimum Spanning Tree.
7. Mark the newly connected vertex as visited.
8. Repeat the process until V - 1 edges are selected.
9. Calculate and display the total minimum cost.
10. If no valid edge is found before all vertices are connected, report that the graph is disconnected.

## Python Program

```python
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

start = int(input("Enter the starting vertex: ")) - 1

prim(graph, start, n)
```

## Sample Input

```text
Enter number of vertices: 4

Enter adjacency matrix:
0 2 4 6
2 0 0 3
4 0 0 5
6 3 5 0

Enter the starting vertex: 1
```

## Sample Output

```text
Edges in Minimum Spanning Tree:
1 - 2 : 2
2 - 4 : 3
1 - 3 : 4
Minimum cost: 9
```

## Explanation

The given graph contains four vertices and the following weighted edges:

| Edge | Weight |
|------|--------|
| 1 - 2 | 2 |
| 1 - 3 | 4 |
| 1 - 4 | 6 |
| 2 - 4 | 3 |
| 3 - 4 | 5 |

Starting vertex: 1

Prim's Algorithm works as follows:

1. Initially, vertex 1 is visited.
2. Among the edges connected to vertex 1, select the minimum-weight edge (1, 2) with weight 2.
3. Now vertices 1 and 2 are visited. Select the minimum-weight edge connecting a visited vertex to an unvisited vertex. Edge (2, 4) has weight 3.
4. Now vertices 1, 2 and 4 are visited. Select edge (1, 3) with weight 4.
5. All four vertices are now connected using three edges. The algorithm terminates.

**Minimum Spanning Tree Cost = 2 + 3 + 4 = 9**

## Important Code Explanation

### 1. Visited Array

```python
visited = [False] * n
visited[start] = True
```

The visited array keeps track of which vertices are already included in the Minimum Spanning Tree.

Initially, all vertices are marked as unvisited. The starting vertex is marked as visited.

### 2. Minimum Weight Initialization

```python
minimum = float('inf')
x = -1
y = -1
```

- `minimum` stores the smallest edge weight found.
- `x` stores the starting vertex of the selected edge.
- `y` stores the ending vertex of the selected edge.

### 3. Finding the Minimum Edge

```python
for i in range(n):
    if visited[i]:
        for j in range(n):
            if not visited[j] and graph[i][j] != 0:
                if graph[i][j] < minimum:
                    minimum = graph[i][j]
                    x = i
                    y = j
```

This part checks all edges connecting visited vertices to unvisited vertices and selects the edge with the minimum weight.

### 4. Adding an Edge to MST

```python
print(x + 1, "-", y + 1, ":", minimum)

total_cost += minimum
visited[y] = True
```

The selected edge is displayed, its weight is added to the total cost, and the newly connected vertex is marked as visited.

### 5. Disconnected Graph Condition

```python
if x == -1:
    print("Graph is disconnected. MST cannot be formed.")
    return
```

If no valid edge is found, the remaining vertices cannot be connected to the current MST. Therefore, a single MST cannot be formed.

## Time Complexity

For this implementation:

| Operation | Complexity |
|-----------|------------|
| Initializing visited array | O(V) |
| Selecting minimum edge | O(V²) per iteration |
| Repeating for V - 1 iterations | O(V³) |
| Overall | **O(V³)** |

Here:
- V = Number of vertices.

**Note:** This complexity is for the specific implementation above, which scans the entire adjacency matrix during every iteration.

## Space Complexity

- Adjacency matrix: O(V²)
- Visited array: O(V)
- Additional variables: O(1)

Overall space complexity, including the input matrix: **O(V²)**.

## Advantages

- Simple and easy to understand.
- Finds the Minimum Spanning Tree using a greedy approach.
- Avoids cycles by connecting visited vertices to unvisited vertices.
- Works well for dense graphs when implemented efficiently.

## Applications

- Designing computer networks.
- Road and railway network planning.
- Electrical power distribution.
- Connecting multiple locations with minimum cost.
- Network cable optimization.

## Result

Thus, Prim's Algorithm was successfully implemented in Python to find the Minimum Spanning Tree of a weighted, undirected graph, and the minimum cost was calculated.
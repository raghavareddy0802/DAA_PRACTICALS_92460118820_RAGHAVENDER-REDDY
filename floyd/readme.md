# Floyd's Algorithm (Floyd–Warshall Algorithm)

## Aim

To implement Floyd's Algorithm to find the shortest distances between all pairs of vertices in a weighted graph using Python.

## Theory

Floyd's Algorithm, also known as the Floyd–Warshall Algorithm, is a dynamic programming algorithm used to find the shortest paths between all pairs of vertices in a weighted graph.

It works by considering each vertex as an intermediate vertex and checking whether travelling through that vertex provides a shorter path.

The algorithm updates the distance matrix by comparing the existing distance with the distance obtained through an intermediate vertex.

It supports both directed and undirected graphs and can handle negative edge weights, but it does not work correctly when the graph contains negative-weight cycles.

In this implementation, an adjacency matrix is used to represent the graph.

- `0` represents the distance from a vertex to itself.
- Positive numbers represent edge weights.
- `999` represents the absence of a direct edge.
- `999` is converted into infinity (`float('inf')`) inside the program.

## Algorithm

1. Start with a weighted graph represented using an adjacency matrix.
2. Read the number of vertices.
3. Read the adjacency matrix from the user.
4. Replace every `999` value with infinity.
5. Create a distance matrix by copying the original graph.
6. Consider each vertex as an intermediate vertex using the outer loop.
7. For every pair of vertices `(i, j)`, calculate the distance through the intermediate vertex `k`.
8. Compare the existing distance with the newly calculated distance.
9. Update the distance if the new path is shorter.
10. Repeat the process for all intermediate vertices.
11. Display the final shortest distance matrix.

## Python Program

```python
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
```

## Sample Input

```text
Enter number of vertices: 4

Enter adjacency matrix (use 999 for no edge):
0 5 999 10
999 0 3 999
999 999 0 1
999 999 999 0
```

## Sample Output

```text
Shortest Distance Matrix:
0 5 8 9
INF 0 3 4
INF INF 0 1
INF INF INF 0
```

## Explanation

The given graph contains four vertices with the following direct edge weights:

| Edge | Weight |
|------|--------|
| 1 - 2 | 5 |
| 1 - 4 | 10 |
| 2 - 3 | 3 |
| 3 - 4 | 1 |

Floyd's Algorithm calculates the shortest distances between every pair of vertices.

The algorithm works as follows:

1. Initially, the distance matrix contains the direct edge weights.
2. Consider vertex 1 as an intermediate vertex and check whether it provides shorter paths.
3. Consider vertex 2 as an intermediate vertex. The path from vertex 1 to vertex 3 becomes shorter through vertex 2.

   Distance = 5 + 3 = 8.

4. Consider vertex 3 as an intermediate vertex. The path from vertex 1 to vertex 4 becomes shorter through vertex 3.

   Distance = 8 + 1 = 9.

5. The path from vertex 2 to vertex 4 also becomes shorter through vertex 3.

   Distance = 3 + 1 = 4.

6. After considering all intermediate vertices, the final shortest distance matrix is displayed.

**Shortest distance from vertex 1 to vertex 4 = 9.**

## Important Code Explanation

### 1. Creating the Distance Matrix

```python
dist = [row[:] for row in graph]
```

This creates a copy of the original adjacency matrix.

The algorithm performs updates on the `dist` matrix while preserving the original graph.

### 2. Three Nested Loops

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
```

These three loops are the main part of Floyd's Algorithm.

- `k` represents the intermediate vertex.
- `i` represents the starting vertex.
- `j` represents the destination vertex.

The algorithm checks every possible pair of vertices through each intermediate vertex.

### 3. Checking for Infinity

```python
if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
```

This condition checks whether both parts of the path exist.

It prevents the program from performing unnecessary calculations with infinity.

### 4. Updating the Shortest Distance

```python
dist[i][j] = min(
    dist[i][j],
    dist[i][k] + dist[k][j]
)
```

This is the main formula of Floyd's Algorithm.

It compares:

- The existing distance between vertices `i` and `j`.
- The distance obtained by travelling through intermediate vertex `k`.

The smaller distance is stored in the distance matrix.

### 5. Displaying the Final Matrix

```python
if dist[i][j] == float('inf'):
    print("INF", end=" ")
else:
    print(dist[i][j], end=" ")
```

If no path exists between two vertices, the program displays `INF`.

Otherwise, it displays the calculated shortest distance.

## Mathematical Formula

The Floyd–Warshall recurrence relation is:

\[
D[i][j] = \min(D[i][j], D[i][k] + D[k][j])
\]

Where:

- `D[i][j]` = Current shortest distance from vertex `i` to vertex `j`.
- `D[i][k]` = Distance from vertex `i` to intermediate vertex `k`.
- `D[k][j]` = Distance from intermediate vertex `k` to vertex `j`.

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Initializing distance matrix | O(V²) |
| Considering intermediate vertices | O(V) |
| Checking all vertex pairs | O(V²) |
| Overall | **O(V³)** |

Here:

- V = Number of vertices.

The algorithm uses three nested loops, so its time complexity is O(V³).

## Space Complexity

- Original adjacency matrix: O(V²)
- Distance matrix: O(V²)
- Additional variables: O(1)

Overall space complexity: **O(V²)**.

## Advantages

- Finds shortest distances between all pairs of vertices.
- Supports negative edge weights.
- Simple implementation using dynamic programming.
- Works with both directed and undirected graphs.
- Does not require a separate algorithm for each starting vertex.

## Limitations

- Cannot correctly calculate shortest paths when a negative-weight cycle exists.
- Has O(V³) time complexity, making it less suitable for very large graphs.
- Requires O(V²) space to store the distance matrix.

## Applications

- Finding shortest routes between multiple locations.
- Network routing and communication systems.
- Transportation and road network optimization.
- Analyzing connectivity in graphs.
- Finding shortest distances in weighted networks.

## Result

Thus, Floyd's Algorithm was successfully implemented in Python to find the shortest distances between all pairs of vertices in a weighted graph using the Floyd–Warshall dynamic programming approach.
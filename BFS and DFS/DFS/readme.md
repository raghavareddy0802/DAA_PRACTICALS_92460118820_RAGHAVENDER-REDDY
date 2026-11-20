# Depth-First Search (DFS)

## Aim

To implement Depth-First Search (DFS) traversal of a graph using Python and an adjacency matrix.

## Theory

Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along one branch before backtracking.

It starts from a selected vertex and visits an unvisited adjacent vertex. This process continues until no unvisited adjacent vertices remain.

After reaching the end of a branch, the algorithm backtracks and explores other unvisited branches.

DFS can be implemented using recursion or an explicit stack. This implementation uses **recursion**, which internally uses the call stack.

A visited array is used to prevent repeated visits to vertices.

## Algorithm

1. Start with a graph represented using an adjacency matrix.
2. Read the number of vertices and the adjacency matrix.
3. Read the starting vertex.
4. Initialize all vertices as unvisited.
5. Call the DFS function with the starting vertex.
6. Mark the current vertex as visited.
7. Display the current vertex.
8. Check all adjacent vertices.
9. If an adjacent vertex is connected and unvisited, recursively call the DFS function for that vertex.
10. Continue until all reachable vertices have been visited.
11. Display the DFS traversal.

## Python Program

```python
def dfs(graph, start, visited, n):
    visited[start] = True

    print(start + 1, end=" ")

    for i in range(n):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited, n)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertex: ")) - 1

visited = [False] * n

print("DFS traversal:")

dfs(graph, start, visited, n)
```

## Sample Input

```text
Enter number of vertices: 5

Enter adjacency matrix:
0 1 1 0 0
1 0 0 1 1
1 0 0 0 0
0 1 0 0 0
0 1 0 0 0

Enter the starting vertex: 1
```

## Sample Output

```text
DFS traversal:
1 2 4 5 3
```

## Explanation

The given graph contains five vertices.

Starting vertex: 1

DFS works as follows:

1. Start from vertex 1 and mark it as visited.
2. Visit the first unvisited adjacent vertex, which is vertex 2.
3. From vertex 2, visit the first unvisited adjacent vertex, which is vertex 4.
4. Vertex 4 has no unvisited adjacent vertices, so backtrack to vertex 2.
5. From vertex 2, visit the next unvisited adjacent vertex, which is vertex 5.
6. Vertex 5 has no unvisited adjacent vertices, so backtrack.
7. Backtrack to vertex 1 and visit the remaining unvisited adjacent vertex, which is vertex 3.
8. Vertex 3 has no unvisited adjacent vertices, so traversal terminates.

**Final DFS Traversal: 1 → 2 → 4 → 5 → 3**

## Important Code Explanation

### 1. Visited Array

```python
visited = [False] * n
```

The visited array keeps track of vertices that have already been visited.

- `False` means the vertex is unvisited.
- `True` means the vertex has been visited.

### 2. Marking the Current Vertex

```python
visited[start] = True
```

The current vertex is marked as visited before exploring its adjacent vertices.

### 3. Displaying the Vertex

```python
print(start + 1, end=" ")
```

The vertex is displayed using its original numbering.

Internally, Python uses zero-based indexing, so `+1` is used to display vertices starting from 1.

### 4. Checking Adjacent Vertices

```python
for i in range(n):
    if graph[start][i] == 1 and not visited[i]:
        dfs(graph, i, visited, n)
```

This checks all vertices connected to the current vertex.

If an adjacent vertex is connected and unvisited, the DFS function is called recursively for that vertex.

### 5. Recursive Function Call

```python
dfs(graph, i, visited, n)
```

This function call moves deeper into the graph.

When no unvisited adjacent vertices are available, the recursive function returns to the previous call. This process is called **backtracking**.

## Time Complexity

For an adjacency matrix implementation:

| Operation | Complexity |
|-----------|------------|
| Initializing visited array | O(V) |
| Checking adjacent vertices | O(V) per vertex |
| Visiting all vertices | O(V²) |
| Overall | **O(V²)** |

Here:
- V = Number of vertices.

## Space Complexity

- Adjacency matrix: O(V²)
- Visited array: O(V)
- Recursive call stack: O(V) in the worst case.

Overall space complexity, including the input matrix: **O(V²)**.

## Advantages

- Simple and easy to implement using recursion.
- Useful for exploring graph structures.
- Requires no separate queue data structure.
- Helps identify cycles and connected components with suitable modifications.

## Applications

- Maze solving.
- Cycle detection in graphs.
- Topological sorting.
- Finding connected components.
- Path finding.
- Exploring network structures.

## Result

Thus, Depth-First Search (DFS) was successfully implemented in Python using an adjacency matrix, and the graph traversal was performed from the given starting vertex.
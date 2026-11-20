# Breadth-First Search (BFS)

## Aim

To implement Breadth-First Search (BFS) traversal of a graph using Python and an adjacency matrix.

## Theory

Breadth-First Search (BFS) is a graph traversal algorithm that explores vertices level by level.

It starts from a selected vertex and visits all its adjacent vertices before moving to the next level.

BFS uses a **Queue data structure** that follows the FIFO (First In, First Out) principle.

A visited array is used to keep track of vertices that have already been visited, preventing repeated visits.

## Algorithm

1. Start with a graph represented using an adjacency matrix.
2. Read the number of vertices and the adjacency matrix.
3. Read the starting vertex.
4. Initialize all vertices as unvisited.
5. Mark the starting vertex as visited.
6. Insert the starting vertex into the queue.
7. Repeat while the queue is not empty:
   - Remove the front vertex from the queue.
   - Display the removed vertex.
   - Check all its adjacent vertices.
   - If an adjacent vertex is connected and unvisited, mark it as visited and insert it into the queue.
8. Continue until the queue becomes empty.
9. Display the BFS traversal.

## Python Program

```python
def bfs(graph, start, visited, n):
    visited[start] = True

    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)

        print(node + 1, end=" ")

        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertex: ")) - 1

visited = [False] * n

print("BFS traversal:")

bfs(graph, start, visited, n)
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
BFS traversal:
1 2 3 4 5
```

## Explanation

The given graph contains five vertices.

Starting vertex: 1

BFS works as follows:

1. Start from vertex 1 and mark it as visited.
2. Insert vertex 1 into the queue.
3. Remove vertex 1 and visit its adjacent vertices 2 and 3.
4. Insert vertices 2 and 3 into the queue.
5. Remove vertex 2 and visit its unvisited adjacent vertices 4 and 5.
6. Insert vertices 4 and 5 into the queue.
7. Remove vertex 3. It has no unvisited adjacent vertices.
8. Remove vertices 4 and 5. No new vertices are found.
9. The queue becomes empty, so traversal terminates.

**Final BFS Traversal: 1 → 2 → 3 → 4 → 5**

## Important Code Explanation

### 1. Visited Array

```python
visited = [False] * n
```

The visited array stores the status of each vertex.

- `False` means the vertex has not been visited.
- `True` means the vertex has already been visited.

### 2. Marking the Starting Vertex

```python
visited[start] = True
```

The starting vertex is marked as visited to prevent it from being added to the queue again.

### 3. Queue Initialization

```python
queue = []
queue.append(start)
```

A queue is created, and the starting vertex is inserted into it.

### 4. Removing an Element

```python
node = queue.pop(0)
```

The `pop(0)` operation removes the first element from the queue, following FIFO order.

### 5. Checking Adjacent Vertices

```python
for i in range(n):
    if graph[node][i] == 1 and not visited[i]:
        visited[i] = True
        queue.append(i)
```

This checks all vertices connected to the current vertex.

If a vertex is connected and has not been visited, it is marked as visited and added to the queue.

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
- Queue: O(V)

Overall space complexity, including the input matrix: **O(V²)**.

## Advantages

- Simple and easy to implement.
- Explores a graph level by level.
- Finds the shortest path in terms of number of edges in an unweighted graph.
- Useful for checking connectivity and reachability.

## Applications

- Shortest path finding in unweighted graphs.
- Social network connections.
- Web crawling.
- Network broadcasting.
- Finding connected components.

## Result

Thus, Breadth-First Search (BFS) was successfully implemented in Python using an adjacency matrix, and the graph traversal was performed from the given starting vertex.# Breadth-First Search (BFS)

## Aim

To implement Breadth-First Search (BFS) traversal of a graph using Python and an adjacency matrix.

## Theory

Breadth-First Search (BFS) is a graph traversal algorithm that explores vertices level by level.

It starts from a selected vertex and visits all its adjacent vertices before moving to the next level.

BFS uses a **Queue data structure** that follows the FIFO (First In, First Out) principle.

A visited array is used to keep track of vertices that have already been visited, preventing repeated visits.

## Algorithm

1. Start with a graph represented using an adjacency matrix.
2. Read the number of vertices and the adjacency matrix.
3. Read the starting vertex.
4. Initialize all vertices as unvisited.
5. Mark the starting vertex as visited.
6. Insert the starting vertex into the queue.
7. Repeat while the queue is not empty:
   - Remove the front vertex from the queue.
   - Display the removed vertex.
   - Check all its adjacent vertices.
   - If an adjacent vertex is connected and unvisited, mark it as visited and insert it into the queue.
8. Continue until the queue becomes empty.
9. Display the BFS traversal.

## Python Program

```python
def bfs(graph, start, visited, n):
    visited[start] = True

    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)

        print(node + 1, end=" ")

        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)


n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter the starting vertex: ")) - 1

visited = [False] * n

print("BFS traversal:")

bfs(graph, start, visited, n)
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
BFS traversal:
1 2 3 4 5
```

## Explanation

The given graph contains five vertices.

Starting vertex: 1

BFS works as follows:

1. Start from vertex 1 and mark it as visited.
2. Insert vertex 1 into the queue.
3. Remove vertex 1 and visit its adjacent vertices 2 and 3.
4. Insert vertices 2 and 3 into the queue.
5. Remove vertex 2 and visit its unvisited adjacent vertices 4 and 5.
6. Insert vertices 4 and 5 into the queue.
7. Remove vertex 3. It has no unvisited adjacent vertices.
8. Remove vertices 4 and 5. No new vertices are found.
9. The queue becomes empty, so traversal terminates.

**Final BFS Traversal: 1 → 2 → 3 → 4 → 5**

## Important Code Explanation

### 1. Visited Array

```python
visited = [False] * n
```

The visited array stores the status of each vertex.

- `False` means the vertex has not been visited.
- `True` means the vertex has already been visited.

### 2. Marking the Starting Vertex

```python
visited[start] = True
```

The starting vertex is marked as visited to prevent it from being added to the queue again.

### 3. Queue Initialization

```python
queue = []
queue.append(start)
```

A queue is created, and the starting vertex is inserted into it.

### 4. Removing an Element

```python
node = queue.pop(0)
```

The `pop(0)` operation removes the first element from the queue, following FIFO order.

### 5. Checking Adjacent Vertices

```python
for i in range(n):
    if graph[node][i] == 1 and not visited[i]:
        visited[i] = True
        queue.append(i)
```

This checks all vertices connected to the current vertex.

If a vertex is connected and has not been visited, it is marked as visited and added to the queue.

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
- Queue: O(V)

Overall space complexity, including the input matrix: **O(V²)**.

## Advantages

- Simple and easy to implement.
- Explores a graph level by level.
- Finds the shortest path in terms of number of edges in an unweighted graph.
- Useful for checking connectivity and reachability.

## Applications

- Shortest path finding in unweighted graphs.
- Social network connections.
- Web crawling.
- Network broadcasting.
- Finding connected components.

## Result

Thus, Breadth-First Search (BFS) was successfully implemented in Python using an adjacency matrix, and the graph traversal was performed from the given starting vertex.
# Travelling Salesperson Problem (TSP)

## Aim

To implement the Travelling Salesperson Problem (TSP) using Python to find the minimum-cost tour that visits every city exactly once and returns to the starting city.

## Theory

The Travelling Salesperson Problem (TSP) is a combinatorial optimization problem in which a salesperson must visit a set of cities exactly once and return to the starting city while minimizing the total travelling cost.

The problem is represented using a weighted cost adjacency matrix, where each element represents the travelling cost between two cities.

In this implementation, the brute-force approach is used.

The algorithm generates all possible visiting orders of the cities, calculates the total cost of each possible tour, and selects the tour with the minimum cost.

The salesperson starts from city 1, visits every other city exactly once, and finally returns to city 1.

## Algorithm

1. Start with a weighted cost adjacency matrix.
2. Read the number of cities.
3. Read the cost adjacency matrix from the user.
4. Fix city 1 as the starting city.
5. Generate all possible permutations of the remaining cities.
6. For each permutation:
   - Initialize the current cost to zero.
   - Start from city 1.
   - Calculate the travelling cost between consecutive cities.
   - Add the cost of returning to the starting city.
7. Compare the current tour cost with the minimum cost.
8. If the current tour cost is smaller, update the minimum cost and best path.
9. Repeat the process for all possible permutations.
10. Display the minimum-cost tour and its total cost.

## Python Program

```python
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
```

## Sample Input

```text
Enter number of cities: 4

Enter cost adjacency matrix:
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```

## Sample Output

```text
Minimum Cost Tour:
1 2 4 3 1
Minimum Cost: 80
```

## Explanation

The given graph contains four cities with the following travelling costs:

| Route | Cost |
|-------|------|
| 1 - 2 | 10 |
| 1 - 3 | 15 |
| 1 - 4 | 20 |
| 2 - 3 | 35 |
| 2 - 4 | 25 |
| 3 - 4 | 30 |

The starting city is fixed as city 1.

The algorithm generates all possible visiting orders of the remaining three cities.

Some possible tours are:

**Tour 1:**

1 → 2 → 3 → 4 → 1

Total Cost = 10 + 35 + 30 + 20 = 95

**Tour 2:**

1 → 2 → 4 → 3 → 1

Total Cost = 10 + 25 + 30 + 15 = 80

**Tour 3:**

1 → 3 → 2 → 4 → 1

Total Cost = 15 + 35 + 25 + 20 = 95

**Tour 4:**

1 → 3 → 4 → 2 → 1

Total Cost = 15 + 30 + 25 + 10 = 80

After checking all possible tours, the minimum travelling cost is found to be 80.

**Minimum Cost Tour = 1 → 2 → 4 → 3 → 1**

**Minimum Cost = 80**

## Important Code Explanation

### 1. Importing Permutations

```python
from itertools import permutations
```

The permutations function generates all possible arrangements of the given cities.

It helps generate every possible visiting order for the salesperson.

### 2. Selecting the Starting City

```python
start = 0
```

The starting city is fixed as city 1.

Python uses zero-based indexing, so city 1 is represented internally by index 0.

### 3. Creating the Remaining Cities List

```python
vertices = []

for i in range(n):
    if i != start:
        vertices.append(i)
```

This creates a list containing all cities except the starting city.

For four cities, the list becomes:

```text
[1, 2, 3]
```

### 4. Initializing Minimum Cost

```python
min_cost = float('inf')
best_path = []
```

- `min_cost` stores the minimum travelling cost found so far.
- `best_path` stores the visiting order of the minimum-cost tour.

Infinity is used initially so that the first valid tour can replace it.

### 5. Generating All Possible Tours

```python
for path in permutations(vertices):
```

This generates every possible permutation of the remaining cities.

For three remaining cities, there are:

3! = 6 possible visiting orders.

### 6. Calculating the Tour Cost

```python
current_cost = 0
k = start

for j in path:
    current_cost += graph[k][j]
    k = j
```

This calculates the travelling cost between consecutive cities.

The variable `k` represents the current city, and `j` represents the next city.

### 7. Returning to the Starting City

```python
current_cost += graph[k][start]
```

After visiting all cities, the salesperson must return to the starting city.

This adds the final travelling cost to the total tour cost.

### 8. Updating the Minimum Cost

```python
if current_cost < min_cost:
    min_cost = current_cost
    best_path = [start] + list(path) + [start]
```

If the current tour has a smaller cost than the previously stored minimum cost, the program updates:

- The minimum cost.
- The best visiting order.

The starting city is added at the beginning and end of the path.

## Time Complexity

For this brute-force implementation:

| Operation | Complexity |
|-----------|------------|
| Generating permutations | O((V - 1)!) |
| Calculating each tour cost | O(V) |
| Checking all possible tours | O(V × (V - 1)!) |
| Overall | **O(V!)** |

Here:

- V = Number of cities.
- (V - 1)! = Number of possible visiting orders when the starting city is fixed.

## Space Complexity

- Cost adjacency matrix: O(V²)
- Remaining cities list: O(V)
- Best path: O(V)
- Current permutation storage: O(V)

Overall space complexity, including the input matrix: **O(V²)**, excluding internal temporary storage used by the permutation iterator.

## Advantages

- Simple and easy to understand.
- Checks every possible visiting order.
- Guarantees the optimal solution for a valid complete cost matrix.
- Useful for understanding combinatorial optimization problems.

## Limitations

- Factorial time complexity makes it inefficient for large numbers of cities.
- The number of possible tours increases rapidly as the number of cities increases.
- Not suitable for large real-world transportation networks.
- Requires significant computation when the number of cities is large.

## Applications

- Route optimization.
- Delivery and logistics planning.
- Transportation network optimization.
- Circuit board manufacturing.
- Vehicle routing and scheduling.
- Planning routes for travelling salespeople.

## Result

Thus, the Travelling Salesperson Problem was successfully implemented in Python using the brute-force approach to find the minimum-cost tour that visits every city exactly once and returns to the starting city.
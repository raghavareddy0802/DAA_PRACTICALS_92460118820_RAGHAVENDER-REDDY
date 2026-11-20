def dfs(graph, start, visited, n):



    visited[start] = True
    print(start+1, end=" ")

    for i in range(n):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i , visited, n)

n = int(input("Enter number of vertices: "))
graph= []

print("Enter adjacency matrix: ")

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

start= int(input("Enter the starting vertex: "))
start = start - 1

visited = [False] * n

print("DFS traversal: ")

dfs(graph, i, visited, n)
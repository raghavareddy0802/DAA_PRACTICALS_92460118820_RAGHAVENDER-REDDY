def bfs(graph, start,visited, n):


    visited[start] = True


    queue = []

    queue.append(start)

    while queue:

        node = queue.pop(0)
        print(node+1,end=" ")

        for i in range(n):

            if graph[node][i] == 1 and not visited[i]:

                visited[i] = True
                queue.append(i)

n = int(input("Enter number of vertices: "))
graph= []
print("Enter the adjacency matrix: ")

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

start = int(input("Enter starting vertex: "))
start = start - 1

visited = [False] * n

print("BFS Traversal: ")

bfs(graph, start, visited, n)
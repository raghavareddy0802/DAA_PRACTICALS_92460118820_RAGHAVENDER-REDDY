d = list(map(int, input("Enter the dimensions array: ").split()))

n = len(d) - 1 
A = []
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        row.append(0)
    A.append(row)

for L in range(2, n + 1):
    for i in range(1, n - L + 2):
        j = i + L - 1
        A[i][j] = float('inf')
      
        for k in range(i, j):
            cost = A[i][k] + A[k + 1][j] + (d[i - 1] * d[k] * d[j])
            if cost < A[i][j]:
                A[i][j] = cost

print("Minimum number of multiplications:", A[1][n])
weights = list(map(int, input("Enter the weights of the items : ").split()))
profits = list(map(int, input("Enter the profits of the items : ").split()))
capacity = int(input("Enter the maximum capacity of the knapsack: "))

n = len(weights)

p = []

for i in range(n + 1):
    row = []
    
    for j in range(capacity + 1):
        row.append(0)
    
    p.append(row)

for i in range(1, n + 1):
    for j in range(1, capacity + 1):
        
        current_weight = weights[i - 1]
        current_profit = profits[i - 1]
        
        if j < current_weight:
            p[i][j] = p[i - 1][j]
        else:
            p[i][j] = max(p[i - 1][j], p[i - 1][j - current_weight] + current_profit)

max_profit = p[n][capacity]

print("Maximum profit that can be obtained:", max_profit)
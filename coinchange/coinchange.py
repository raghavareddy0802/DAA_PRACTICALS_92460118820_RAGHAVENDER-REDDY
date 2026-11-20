coins = list(map(int, input("Enter the coin values: ").split()))
amount = int(input("Enter the target amount: "))

n = len(coins)

c = []
for i in range(n + 1):
    row = []
    for j in range(amount + 1):
        row.append(0)
    c.append(row)

for j in range(1, amount + 1):
    c[0][j] = float('inf')

for i in range(1, n + 1):
    di = coins[i - 1] 
    for j in range(1, amount + 1):
        if j < di:
            c[i][j] = c[i - 1][j]
        else:
            c[i][j] = min(c[i - 1][j], 1 + c[i][j - di])

result = c[n][amount]
if result == float('inf'):
    print("Not possible to make the target amount with given coins.")
else:
    print("Minimum number of coins:", result)
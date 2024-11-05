def knapsack(weights,values,capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(values)):
        for w in range(capacity,weights[i]-1,-1):
            dp[w] = max(dp[w],dp[w-weights[i]]+values[i])

    return dp[capacity]

n=int(input("Enter the number of items:- "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter the weight of {i+1} item: "))
    value = int(input(f"Enter the values of {i+1} item: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity: "))

max_profit = knapsack(weights,values,capacity)

print(f"The max profit in knapsack is {max_profit}")
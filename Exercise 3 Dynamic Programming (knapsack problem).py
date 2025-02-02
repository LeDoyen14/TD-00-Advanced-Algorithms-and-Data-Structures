def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(max_weight + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1]+dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][max_weight]


# Example Test Case
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
max_weight = 6
print("Maximum value", knapsack(weights, values, max_weight))

# Basic Solution #
def solve_knapsack1(profits, weights, capacity):
    return knapsack_recursive1(profits, weights, capacity, 0);

def knapsack_recursive1(profits, weights, capacity, currentIndex):
    # base case
    if (capacity <= 0 or currentIndex >= len(profits)):
        return 0

    # recursive call after choosing the elements at the currentIndex ...
    # if the weight of the element at currentIndex exceeds the capacity ...
    # we should'nt process 
    profit_a = 0
    if (weights[currentIndex] <= capacity):
        profit_a = profits[currentIndex] + knapsack_recursive1(profits, weights, capacity - weights[currentIndex], currentIndex + 1)
    
    # recursive call after excluding the elements at the currentIndex
    profit_b = knapsack_recursive1(profits, weights, capacity, currentIndex + 1)

    return max(profit_a, profit_b)

def solve_knapsack2(profits, weights, capacity):
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive2(dp, profits, weights, capacity, 0)

def knapsack_recursive2(dp, profits, weights, capacity, index):
    # base checks
    if (capacity <= 0 or index >= len(profits)):
        return 0
    
    # if we have already solved a simila
    if (dp[index][capacity] != -1):
        return dp[index][capacity]

    # recursive call after choosing the element at the current index
    # if the weight of the element at current index exceeds the capacity,
    # we shouldn't process this
    profit_a = 0
    if (weights[index] <= capacity):
        profit_a = profits[index] + knapsack_recursive2(dp, profits, weights, capacity - weights[index], index + 1)
    
    # recursive call after excluding the elements at the index
    profit_b = knapsack_recursive2(dp, profits, weights, capacity, index + 1)

    dp[index][capacity] = max(profit_a, profit_b)
    return dp[index][capacity]

def solve_knapsack3(profits, weights, capacity):
    n = len(profits)
    
    if (capacity <= 0 or n == 0 or len(weights) != n):
        return 0
    
    dp = [[0 for x in range(capacity + 1)] for y in range(n)]

    # populate the capacity = 0 columns with '0' capacity we have '0' profit
    for i in range(0, n):
        dp[i][0] = 0
    
    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity + 1):
        if (weights[0] <= c):
            dp[0][c] = profits[0]
    
    for i in range(1, n):
        for c in range(1, capacity + 1):
            profit_a, profit_b = 0, 0
            if (weights[i] <= c):
                profit_a = profits[i] + dp[i-1][c-weights[i]]
            profit_b = dp[i-1][c]
            dp[i][c] = max(profit_a, profit_b)
    
    return dp[n-1][capacity]
 
if __name__ == '__main__':
    weights = [2,3,1,4]
    profits = [4,5,3,7]
    capacity = 5
    print("Basic Knapsack: ", solve_knapsack1(profits, weights, capacity))
    print("TopDown Knapsack: ", solve_knapsack2(profits, weights, capacity))
    print("BottomUp Knapsack: ", solve_knapsack3(profits, weights, capacity))
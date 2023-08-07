def can_partition(num):
    s = sum(num)
    # if 's' is an odd number, we can't have two subsets with the same total
    if s % 2 != 0:
        return False
    
    # we are trying to find a subset of given numbers that has a total of 's/2'
    s = int(s / 2)
    n = len(num)
    dp = [[False for x in range(s + 1)] for y in range(n)]

    # populate the sum=0 column, as we can always have '0' sum without including any element
    for i in range(0, n):
        dp[i][0] = True
    
    # with only one number, we can form a subset only when the required sum is equal to its value
    for j in range (1, s+1):
        dp[0][j] = num[0] == j
    
    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, s + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if (dp[i-1][j]):
                dp[i][j] = dp[i-1][j]
            elif (num[i] <= j):
                dp[i][j] = dp[i-1][j- num[i]]
    return dp[n-1][s]

if __name__ == '__main__':
    input_a = [1,5,11,5]
    print("Can Partition: ", can_partition(input_a))
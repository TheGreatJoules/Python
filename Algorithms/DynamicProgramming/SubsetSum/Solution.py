def can_partition_a(num, sum):
    n = len(num)
    dp = [[False for y in range(sum + 1)] for x in range(n)]

    # populate the sum = 0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] =True
    
    # with only one number, we can form a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        dp[0][s] = True if num[0] == s else False

    # process all subsets for all sums
    for i in range(1, n):
        for s in range(1, sum + 1):
            # if we can get the sum 's' without the number at index 'i'
            if (dp[i - 1][s]):
                dp[i][s] = dp[i - 1][s]
            elif s >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][s] = dp[i-1][s - num[i]]
    # return the bottom right corner
    return dp[n - 1][sum]

# Alternative approach that utilizes less memory
def can_partition_b(num, sum):
    n = len(num)
    dp = [False for x in range(sum + 1)]

    # handle sum=0 as we can always have '0' sum with an empty set
    dp[0] = True

    # with only one number, we can have a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        dp[s] = num[0] == s
    
    # process all subsets for all sums
    for i in range(1, n):
        for s in range(0, sum + 1):
            # if dp[s] == true, this means we can get the sum 's' without num[i]
            # the next number else we can include num[i] and see if we can find a subset to get the remaining sum
            if (not dp[s] and s >= num[i]):
                dp[s] = dp[s - num[i]]
    
    return dp[sum]

if __name__ == '__main__':
    input = [1,2,3,7]
    sum = 6
    print("CanPartitionA: ", can_partition_a(input, sum))
    print("CanPartitionB: ", can_partition_b(input, sum))
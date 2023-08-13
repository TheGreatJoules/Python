def can_partition_a(num):
  return can_partition_recursive_a(num, 0, 0, 0)


def can_partition_recursive_a(num, currentIndex, sum1, sum2):
  # base check
  if currentIndex == len(num):
    return abs(sum1 - sum2)

  # recursive call after including the number at the currentIndex in the first set
  diff1 = can_partition_recursive_a(
    num, currentIndex + 1, sum1 + num[currentIndex], sum2)

  # recursive call after including the number at the currentIndex in the second set
  diff2 = can_partition_recursive_a(
    num, currentIndex + 1, sum1, sum2 + num[currentIndex])

  return min(diff1, diff2)

def can_partition_b(num):
    s = sum(num)
    dp = [[-1 for y in range(s+1)] for y in range(len (num))]
    return can_partition_recursive_b(dp, num, 0, 0, 0)

def can_partition_recursive_b(dp, num, index, sum_a, sum_b):
    # base check
    if index == len(num):
        return abs(sum_a - sum_b)
    
    # check if we have not already processed similar problem
    if (dp[index][sum_a] == -1):
        # recursive call after including the number at the index in the first set
        diff_a = can_partition_recursive_b(dp, num, index + 1, sum_a + num[index], sum_b)
        
        # recursive call after including the number at the index in the second set
        diff_b = can_partition_recursive_b(dp, num, index + 1, sum_a, sum_b + num[index])

        dp[index][sum_a] = min(diff_a, diff_b)
    
    return dp[index][sum_a]

def can_partition_c(num):
    s = sum(num)
    n = len(num)
    dp = [[False for y in range(int(s/2) + 1)] for x in range(n)]
    # populate the s=0 columns, as we can always form '0' sum with an empty set
    for i in range(0, n):
        dp[i][0] = True
    
    # with only one number, we can form a subset only when the required sum is equal to the number
    for j in range(0, int(s/2) + 1):
        dp[0][j] = True if num[0] == j else False

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, int(s/2) + 1):
            if (dp[n-1][j]):
                dp[i][j] = dp[i-1][j]
            elif j >= num[i]:
                # else include the number and see if we can find a subset to get the remaining sum
                dp[i][j] = dp[i-1][j - num[i]]
    
    sum_a = 0
    for i in range(int(s/2), -1, -1):
        if (dp[n-1][i]):
            sum_a = i - 1
            break
    
    sum_b = s/2 - sum_a - 1
    return abs(sum_b - sum_a)

if __name__ == '__main__':
    input = [1,2,3,4]
    print("BruteForce: ", can_partition_a(input))
    print("TopDown: ", can_partition_b(input))
    print("BottomUp: ", can_partition_c(input))
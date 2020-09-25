''' 

Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return the minimum number of moves needed to remove all numbers from the array.

''' 



class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[n for _ in range(n)] for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
#                 every number is a palindrome of itself
                if l == r:
                    dp[l][r] = 1
#                      handles cases like 12
                elif l + 1 == r:
                    dp[l][r] = 2
#                     handles cases like 11
                    if arr[l] == arr[r]:
                        dp[l][r] = 1
                else:
                    dp[l][r] = min(
                        dp[l + 1][r - 1] + (0 if arr[l] == arr[r] else 2),
                        dp[l][r], dp[l + 1][r] + 1,
                        dp[l][r - 1] + 1)
                    for k in range(l, r):
                        dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])
        print(dp)
        return dp[0][n - 1]
        
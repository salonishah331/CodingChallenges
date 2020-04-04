
'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Time complexity : O(mn)O(mn). Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once. The total time complexity is then O(V+E)O(V+E). VV is the total number of vertices and EE is the total number of edges. In our problem, O(V) = O(mn)O(V)=O(mn), O(E) = O(4V) = O(mn)O(E)=O(4V)=O(mn).

Space complexity : O(mn)O(mn). The cache dominates the space complexity.

'''




def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        res = 0
        dp = {}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, self.helper(matrix, i, j, dp))
        
        return res
        
    
    def helper(self, matrix, i, j, dp):
        if (i, j) in dp:
            return dp[(i, j)]
        
        res = 0
        
        if i > 0 and matrix[i-1][j] > matrix[i][j]:
            res = max(res, self.helper(matrix, i-1, j, dp))
        
        if j > 0 and matrix[i][j-1] > matrix[i][j]:
            res = max(res, self.helper(matrix, i, j-1, dp))
        
        if i < len(matrix)-1 and matrix[i+1][j] > matrix[i][j]:
            res = max(res, self.helper(matrix, i+1, j, dp))
        
        if j < len(matrix[0])-1 and matrix[i][j+1] > matrix[i][j]:
            res = max(res, self.helper(matrix, i, j+1, dp))
        
        dp[(i, j)] = res + 1
        
        return res + 1

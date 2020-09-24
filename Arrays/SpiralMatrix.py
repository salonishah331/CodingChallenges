'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

'''



class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        T = 0
        B = len(matrix) - 1
        L = 0
        R = len(matrix[0]) - 1
        direction = 0
        outputArr = []
        
        while L <= R and T <= B:
            if direction == 0:
                for k in range(L, R+1):
                    outputArr.append(matrix[T][k])
                T += 1
            if direction == 1:
                for k in range(T,B+1):
                    outputArr.append(matrix[k][R])
                R -= 1
            if direction == 2:
                for k in range(R,L-1, -1):
                    outputArr.append(matrix[B][k])
                B -= 1
            if direction == 3:
                for k in range(B,T-1,-1):
                    outputArr.append(matrix[k][L])
                L += 1
            direction = (direction + 1)%4
        return outputArr
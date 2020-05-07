'''
Pascal's Triangle
'''



class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            triangle = [[1], [1,1]]
            prevmid = [1, 1]
            mid = [1]
            for x in range (numRows -2):
                for i in range(len(prevmid) -1):
                    if prevmid[i + 1]:
                        mid.append(prevmid[i] + prevmid[i+1])
                mid.append(1)
                triangle.append(mid)
                prevmid = mid
                mid = [1]
            return triangle
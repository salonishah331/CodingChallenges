'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
#                 first half is non-rotated
                if target >= nums[start] and target < nums[mid]:
#                     if mid is located in left subarray
                    end = mid - 1
                else:
                    start = mid + 1
#                 second half is non-rotated
            else:
                if target <= nums[end] and target > nums[mid]: 
#                     if mid is located in right subarray
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
        
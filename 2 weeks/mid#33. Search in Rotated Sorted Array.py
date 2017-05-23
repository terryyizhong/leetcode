'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        start, end = nums[l], nums[r]
        while l <= r:       # when use equal here, r = mid - 1
            mid = (l+r) / 2
            curr = nums[mid]
            if curr == target:
                return mid
            if curr >= start:       # determine curr search in which sorted subarray
                if target >= start and target < curr:     # the only case search to the left
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target <= end and target > curr:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

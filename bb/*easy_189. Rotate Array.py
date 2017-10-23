'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k] 
        ############## nums = nums[-k:] + nums[:-k] because this only change the reference nums to new list
        ############## only use nums[:] can in-place change the original list  

#Classical 3-step array rotation:
'''
reverse the first n - k elements
reverse the rest of them
reverse the entire array     
O(n) in time, O(1) in space


'''
#Iterative and improved solution:

#put the last k elements in correct position (ahead) and do the remaining n - k. Once finish swap, the n and k decrease.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in xrange(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
            n, j = n - k, j + k
            k = k % n
#O(n) in time, O(1) in space

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])     # if use sum as a variable in code, even after use as function, will cause compile error
        for i in range(len(nums) - 2):  # last check will be last 3 ele
            k, j = i + 1, len(nums) - 1 
            while k < j:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == target:
                    return target
                if abs(sum3 - target) < abs(ans - target):
                    ans = sum3
                if sum3 > target:
                    j -= 1
                else:
                    k += 1
        return ans
        
            

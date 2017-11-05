'''
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
'''
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """   
        nums = [i for i in str(n)]
        cur_max = 0
        i = j = len(nums) - 1
        while i >= 0:
            if int(nums[i]) < cur_max:
                break
            cur_max = int(nums[i])
            i -= 1
        if i >= 0:  # if no exist, eg. 21. i will be -1, becase no descending in the loop
            while j > i:
                if int(nums[j]) > int(nums[i]):
                    break
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            ans = int(''.join(nums[:i+1] + nums[i+1:][::-1]))   # aware the type change
            return ans if ans < pow(2, 31) else -1    # 32 bit, need smaller than pow(2, 31)
        return -1
        
        
        
        
        

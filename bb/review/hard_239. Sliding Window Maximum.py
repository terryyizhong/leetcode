'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        ans = []
        for i, v in enumerate(nums):
            while deque and v >= nums[deque[-1]]:  # make sure the most left is curr window's max, if larger, can dele the end, else should                                                            keep in it beacuse could be the max of latter window
                deque.pop()
            deque.append(i)   
            if i - k == deque[0]:   # if deque has ele's index out of window popleft
                deque.popleft()
            if i >= k - 1:    # after i >= k -1, each itearation append the curr window's max
                ans.append(nums[deque[0]])
        return ans
                
        
            
        

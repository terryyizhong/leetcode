'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

#O(N) best case / O(N^2) worst case running time + O(1) memory
#The smart approach for this problem is to use the selection algorithm (based on the partion method - the same one as used in quicksort).
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, l, r):
            low = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[low] = nums[low], nums[i]
                    low += 1
            nums[low], nums[r] = nums[r], nums[low]
            return low
        
        l, r, n = 0, len(nums), len(nums)
        while l < r:
            tmp_k = partition(nums, l , r - 1)
            if n - tmp_k == k:
                break
            if n - tmp_k > k:
                l = tmp_k + 1
            else:
                r = tmp_k
        return nums[n-k]
        
# if k is small, can use O(nk) time bubble sort        

'''
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''
'''
What if the given array is already sorted? How would you optimize your algorithm?
just used 2 pointers solution

What if nums1's size is small compared to nums2's size? Which algorithm is better?
make a hashmap stored nums1 and check in nums2

What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

If only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that fit into the memory, and record the intersections.

#I think the second part of the solution is impractical, if you read 2 elements at a time, this procedure will take forever. In principle, we want minimize the number of disk access during the run-time.
An improvement can be sort them using external sort, read (let's say) 2G of each into memory and then using the 2 pointer technique, then read 2G more from the array that has been exhausted. Repeat this until no more data to read from disk.

#I think the goal of this question is to test whether the interview understands some of the data engineering techniques. From a data engineer's perspective, basically there are three ideas to solve the question:

Store the two strings in distributed system(whether self designed or not), then using MapReduce technique to solve the problem;

Processing the Strings by chunk, which fits the memory, then deal with each chunk of data at a time;

Processing the Strings by streaming, then check.
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ans = set()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(ans)
        
        
'''
Solution 1:

use set operation in python, one-line solution.

class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    return list(set(nums1) & set(nums2))
Solution 2:

brute-force searching, search each element of the first list in the second list. (to be more efficient, you can sort the second list and use binary search to accelerate)

class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums1:
        if i not in res and i in nums2:
            res.append(i)
    
    return res
Solution 3:

use dict/hashmap to record all nums appeared in the first list, and then check if there are nums in the second list have appeared in the map.

class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    map = {}
    for i in nums1:
        map[i] = map[i]+1 if i in map else 1
    for j in nums2:
        if j in map and map[j] > 0:
            res.append(j)
            map[j] = 0
    
    return res
Solution 4:

sort the two list, and use two pointer to search in the lists to find common elements.

class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    nums1.sort()
    nums2.sort()
    i = j = 0
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            if not (len(res) and nums1[i] == res[len(res)-1]):
                res.append(nums1[i])
            i += 1
            j += 1
    
    return res
'''

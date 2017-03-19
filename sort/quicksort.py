
def quick_sort(nums):
    return quick(nums, 0, len(nums)-1)


def quick(nums, left, right):
    if left >= right:       # base case: only 1 or 0 element in the interval of unsorted index range
        return nums
    curr = nums[left]
    l, r = left, right      # canot use l = left + 1 in here or the end index of the loop can be larger than curr
    while l < r:        # use l < r in any cases
        while curr <= nums[r] and l < r:      #test right index first or will cause the last one not be checked
            r -= 1
        while curr >= nums[l] and l < r:
            l += 1
        nums[l], nums[r] = nums[r], nums[l]
    nums[left], nums[l] = nums[l], nums[left]         #end ponit must small or equal to curr
    quick(nums, left, r-1)      # transmit nums each time so that can be done "in place" just change in nums and after all the quick, will                                         become a sorted nums
    quick(nums, r+1, right)     # can not contain curr in next recursive or will not end in some case
    return nums

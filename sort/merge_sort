def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = (len(nums)) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(l, r):
    # if not l:                         no need for this debug
    #     return r
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    if j == len(r):
        result.append(l[i:])
    else:
        result.append(r[j:])
    return result

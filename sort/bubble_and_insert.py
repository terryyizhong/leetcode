def bubble_sort(nums):
    # 算法思想：每次从最后开始往前滚，邻接元素两两相比，小元素交换到前面,
    # 第一轮循环把最小的元素上浮至第一个位置，第二小的元素上浮至第二个位置，依次类推
    l = len(nums) - 1
    i = 0
    while i < l:
        back = l
        while back > i:
            if nums[back] < nums[back-1]:
                nums[back-1], nums[back] = nums[back], nums[back-1]
            back -= 1
        i += 1
    return nums

def insert_sort(nums):
    for i in range(1, len(nums)):
        curr = nums[i]
        index = 0       #set to zero, or if curr < all the numbers before it, will not go in to the code inside 'else'
        for j in range(i-1, -1, -1):
            if curr < nums[j]:
                nums[j+1] = nums[j]
            else:
                index = j+1
                break
        nums[index] = curr
    return nums

def bubbleSort(nums):
    count = len(nums) - 2
    while count > 0:
        for i in range(count + 1):
            if nums[i] > nums[i + 1]:
                nums[i],nums[i + 1] = nums[i + 1], nums[i]
        count -= 1
    return nums
print bubbleSort('121')

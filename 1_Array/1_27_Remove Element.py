def removeElement(nums, val):
    
    # i为慢指针
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i = i + 1

    return i

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))
print(nums)
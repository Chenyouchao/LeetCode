def removeDuplicates(nums):

    i = 0
    count = 1
    for j in range(1, len(nums)):
        if nums[j] == nums[j-1]:
            count = count + 1
        else:
            count = 1

        # [1,2,3,4]
        # [1,1,2,3,4,5]
        # [1,1,1,1,2,3]
        if count <= 2:
            i = i + 1
            nums[i] = nums[j]
                      
    return i + 1

nums = [0,0,1,1,1,1,2,3,3]

print(removeDuplicates(nums))
print(nums)
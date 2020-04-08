# O(N), O(1) 
def firstMissingPositive(nums):

    len_ = len(nums)

    flag = False     # 默认不含有1
    for i in range(len_):
        if nums[i] == 1:
            flag = True
            break
    
    if flag is False:
        return 1        # if return 逻辑反转

    if len_ == 1:
        return 2

    # 以下为含有1, 且长度>=2的数组
    for i in range(len_):
        if nums[i] <= 0 or nums[i] > len_:
            nums[i] = 1

    for i in range(len_):
        # 将自身作为bitmap
        # 第n位的正负号代表n是否存在, 存在为负
        # [1,-2,3,-4]
        nums[abs(nums[i])-1] = - abs(nums[abs(nums[i])-1])

    for i in range(len_):
        if nums[i] > 0:
            return i + 1

    return len_ + 1 

    
nums = [3,4,-1,1]

print(firstMissingPositive(nums))
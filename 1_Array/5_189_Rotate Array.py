# O(n), O(1), 93.3%, 98.46%
def rotate(nums, k):

    nums[:] = nums[len(nums)-k: ] + nums[: len(nums)-k]


# O(n * k), O(1)
def rotate_1(nums, k):

    len_ = len(nums)
    for i in range(k):
        temp = nums[len_-1]
        for j in range(len_-1):
            nums[len_-j-1] = nums[len_-j-2]
        nums[0] = temp


nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)
print(nums)
nums = input().split(' ')
nums = [int(i) for i in nums]   
def maxAlternatingSum(nums):
    n = len(nums)
    if n == 1:return nums[0]
    pos = 0
    res = 0
    while True:
        while pos < n - 1 and nums[pos+1] > nums[pos]:
            pos += 1
        res += nums[pos]
        if pos == n - 1:
            break
        pos += 1
        while pos < n - 1 and nums[pos+1] <= nums[pos]:
            pos += 1
        if pos == n - 1:
            break
        res -= nums[pos]
    return res

print(maxAlternatingSum(nums))
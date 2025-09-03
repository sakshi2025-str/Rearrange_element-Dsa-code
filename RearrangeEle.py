# rearrange elements by sign
def rearrangeelements(nums):
    n = len(nums)
    ans = [0]*n
    posIdx,negIdx = 0,1
    for i in range(n):
        if nums[i] < 0:
            ans[negIdx] = nums[i]
            negIdx += 2
        else:
            ans[posIdx] = nums[i]
            posIdx += 2
    return ans

nums = list(map(int,input("enter the array:").split()))
print("after rearrange element," , rearrangeelements(nums))
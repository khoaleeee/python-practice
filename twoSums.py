def twoSums(nums, target):
    seen={}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
nums = [1,2,3,4,5]
target = 5
print(twoSums(nums,target))
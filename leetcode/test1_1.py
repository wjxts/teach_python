# nums = [0,0,1,1,1,2,2,3,3,4]
# a = -10001
# j = 0
# for i in range(len(nums)):
#     if nums[i] != a:
#         a = nums[i]
#         nums[j] = nums[i]
#         j += 1
        
    
# print(nums[0:j])

nums = [0,1,2,2,3,0,4,2]
j = 0
val = 2
for i in range(len(nums)):
    if nums[i] != val:
        nums[j] = nums[i]
        j += 1
    
print(nums)
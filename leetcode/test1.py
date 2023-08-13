nums = [0,0,1,1,1,2,2,3,3,4]
a = []
cnt = 0
i = 0
while (i - cnt) < len(nums):
    if nums[i - cnt] in a:
        nums.pop(i - cnt)
        cnt += 1
    else:
        a.append(nums[i - cnt])
    i += 1

print(nums, cnt)


        
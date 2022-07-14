n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j] :
            nums[i], nums[j] = nums[j], nums[i]

for N in nums:
    print(N)
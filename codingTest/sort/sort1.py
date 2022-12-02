n = int(input())
nums = []
for i in range(n):
    nums.append(input())

print(sorted(nums, reverse=True))
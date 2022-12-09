def solution(nums):
    length = len(nums)/2
    nums = set(nums)
    if len(nums) < length:
        return len(nums)
    else:
        return length
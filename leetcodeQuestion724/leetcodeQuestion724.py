from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rSum = 0
        for i in nums:
            rSum += i
        lSum = 0
        i = 0
        for i in range(len(nums)):
            rSum -= nums[i]
            if(lSum == rSum):
                return i
            lSum += nums[i]
        return -1

    def __init__(self, nums: List[int]) -> None:
        print(self.pivotIndex(nums))


arr = [-1, -1, 0, 1, 1, 0]
Solution(arr)

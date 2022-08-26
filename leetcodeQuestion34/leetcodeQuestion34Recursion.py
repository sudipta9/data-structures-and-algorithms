from typing import List


class Solution:
    def findLeftPos(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start == end and nums[start] != target:
            return -1
        leftPos = -1
        mid = start + ((end - start) // 2)
        if nums[mid] == target:
            return mid

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass

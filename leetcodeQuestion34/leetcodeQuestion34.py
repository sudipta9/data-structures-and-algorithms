from typing import List


class Solution:
    def firstOccurrence(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        leftPos = -1
        while start <= end:
            mid = start + ((end - start) // 2)
            if target == nums[mid]:
                leftPos = mid
                end = mid - 1
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        return leftPos

    def lastOccurrence(self, nums: List[int], target: int):
        start = 0
        end = len(nums) - 1
        rightPos = -1
        while start <= end:
            mid = start + ((end - start) // 2)
            if target == nums[mid]:
                rightPos = mid
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        return rightPos

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result: List[int] = []
        result.append(self.firstOccurrence(nums, target))
        result.append(self.lastOccurrence(nums, target))
        return result

    def __init__(self, nums: List[int], target: int) -> None:
        print(self.searchRange(nums, target))


arr = [1, 2, 3, 3, 3, 4, 7]
Solution(arr, 1)

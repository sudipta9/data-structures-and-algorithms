from typing import List


class Solution:
    def findPivot(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = start + ((end - start) // 2)
        while start < end:
            if(nums[mid] >= nums[0]):
                start = mid + 1
            else:
                end = mid
            mid = start + ((end - start) // 2)
        return mid

    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        pivot = self.findPivot(nums)
        if nums[pivot] == target:
            return pivot
        elif target > nums[pivot] and target <= nums[end]:
            return self.binarySearch(nums, target, pivot, end)
        else:
            return self.binarySearch(nums, target, start, pivot)

    def __init__(self, nums: List[int], target: int) -> None:
        print(self.search(nums, target))


# arr = [4, 5, 6, 7, 0, 1, 2]
arr = [5, 1, 3]
Solution(arr, 3)

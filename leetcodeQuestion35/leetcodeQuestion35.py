from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # liner search approach
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i

        # binary search
        left = 0
        right = len(nums)
        ans = -1
        while left <= right - 1:
            mid = left + ((right - left) // 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                ans = mid
                right = mid
            else:
                left = mid + 1
                ans = mid + 1
        return ans

    def __init__(self) -> None:
        nums = [1, 3]
        target = 0
        print(self.searchInsert(nums, target))


Solution()

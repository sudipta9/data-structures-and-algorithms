from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if (arr[mid] > arr[mid - 1] and arr[mid + 1] < arr[mid]):
                return mid
            elif arr[mid] < arr[mid-1]:
                end = mid
            elif arr[mid] < arr[mid + 1]:
                start = mid + 1

    def __init__(self, arr: List[int]) -> None:
        print(self.peakIndexInMountainArray(arr))


arr = [3, 9, 8, 6, 4]
Solution(arr)

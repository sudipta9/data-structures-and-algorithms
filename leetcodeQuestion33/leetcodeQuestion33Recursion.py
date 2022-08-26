from typing import List


def findPivot(numsArr: List[int], start: int, end: int) -> int:
    if start == end:
        return start
    mid = start + ((end - start) // 2)
    if numsArr[0] <= numsArr[mid]:
        return findPivot(numsArr, mid + 1, end)
    else:
        return findPivot(numsArr, start, mid)


def bs(numsArr: List[int], start: int, end: int, target: int) -> int:
    if start == end and numsArr[start] != target:
        return -1
    mid = start + ((end - start) // 2)
    if numsArr[mid] == target:
        return mid
    if numsArr[mid] > target:
        return bs(numsArr, start, mid, target)
    else:
        return bs(numsArr, mid + 1, end, target)


def search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    pivot = findPivot(nums, start, end)
    if nums[pivot] == target:
        return pivot
    if target > nums[pivot] and target <= nums[end]:
        return bs(nums, pivot, end, target)
    else:
        return bs(nums, start, pivot, target)


arr = [1]
print(search(arr, 0))

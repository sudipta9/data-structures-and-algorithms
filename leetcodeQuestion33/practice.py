from typing import List


def findPivot(numsArray: List[int]) -> int:
    start = 0
    end = len(numsArray) - 1
    mid = start + ((end - start) // 2)
    while start < end:
        if numsArray[mid] >= numsArray[0]:
            start = mid + 1
        else:
            end = mid - 1
        mid = start + ((end - start) // 2)
    return mid


def binarySearch(numsArray: List[int], target: int, start: int, end: int) -> int:
    mid = start + ((end - start) // 2)
    while start <= end:
        if numsArray[mid] == target:
            return mid
        if numsArray[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
        mid = start + ((end - start) // 2)
    return -1


def search(numsArr: List[int], target: int) -> int:
    start = 0
    end = len(numsArr) - 1
    pivot = findPivot(numsArr)
    if numsArr[pivot] == target:
        return pivot
    if target > numsArr[pivot] and target <= numsArr[end]:
        return binarySearch(numsArr, pivot + 1, end)
    else:
        return binarySearch(numsArr, target, start, pivot - 1)


arr = [4, 5, 6, 7, 0, 1, 2]
print(search(arr, 7))

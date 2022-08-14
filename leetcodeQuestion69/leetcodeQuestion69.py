class Solution:
    def sqrt(self, x: int) -> int:
        start = 0
        end = x
        ans = -1
        while start <= end:
            mid = start + ((end - start) // 2)
            sqrMid = mid * mid
            if sqrMid == x:
                return mid
            if sqrMid < x:
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans

    def __init__(self, x) -> None:
        print(self.sqrt(x))


Solution(8)

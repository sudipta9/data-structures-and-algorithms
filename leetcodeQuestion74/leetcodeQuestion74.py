from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     start = 0
        #     end = len(matrix[i]) - 1
        #     while start <= end:
        #         mid = start + ((end - start) // 2)
        #         if matrix[i][mid] == target:
        #             return True
        #         elif matrix[i][mid] > target:
        #             end = mid - 1
        #         else:
        #             start = mid + 1
        # return False

        i = len(matrix[0]) - 1
        r = 0
        flag = False
        while i >= 0 and r < len(matrix):
            if matrix[r][i] == target:
                flag = True
                break
            elif matrix[r][i] > target:
                i = i - 1
            else:
                r += 1
        return flag

    def __init__(self) -> None:
        matrix, target = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 10
        print(self.searchMatrix(matrix, target))


Solution()

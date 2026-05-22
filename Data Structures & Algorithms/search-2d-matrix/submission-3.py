import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = bisect.bisect_right(list(map(lambda x: x[0], matrix)), target)
        print(index)
        if index < len(matrix) and matrix[index][0] == target: return True
        index -= 1
        index2 = bisect.bisect_right(matrix[index], target)
        print(index2)
        if index2 < len(matrix[index]) and matrix[index][index2] == target: return True
        index2 -= 1
        return matrix[index][index2]==target
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for j in range(n // 2):
            for i in range(j, n - j - 1):
                a = matrix[j][i]
                b = matrix[i][-j-1]
                c = matrix[-j-1][-i-1]
                d = matrix[-i-1][j]
                # print(i, j, a, b, c, d)
                matrix[i][-j-1] = a
                matrix[-j-1][-i-1] = b
                matrix[-i-1][j] = c
                matrix[j][i] = d
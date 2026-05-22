class Solution:
    def minAfter(self, arr: List[int]) -> List[int]:
        result = [0] * len(arr)
        arr = [-1] + arr + [-1]
        a = [(0, -1)]
        for i, x in enumerate(arr[1:]):
            i = i + 1
            if a and x < a[-1][1]:
                while x < a[-1][1]:
                    result[a[-1][0]-1] = i-1
                    a.pop()
            a.append((i, arr[i]))

        return result
    def largestRectangleArea(self, heights: List[int]) -> int:
        a = self.minAfter(heights)
        print(a)
        b = list(map(lambda x: len(heights) - 1 - x, self.minAfter(heights[::-1])))[::-1]
        return max(abs((a[i] - b[i] - 1)) * h for i, h in enumerate(heights))

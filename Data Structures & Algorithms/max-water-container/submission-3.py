class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        m = min(heights[start], heights[end]) * (end - start)
        while end > start:
            if heights[start] < heights[end]:
                start += 1
            elif heights[end] < heights[start]:
                end -= 1
            else: start += 1
            m = max(m, min(heights[start], heights[end]) * (end - start))

        return m

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [n - 1] * n

        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                right[stack.pop()] = i - 1
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        return max((right[i] - left[i] + 1) * h for i, h in enumerate(heights))
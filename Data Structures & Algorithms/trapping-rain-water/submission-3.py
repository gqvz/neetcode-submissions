class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        start = 0
        end = len(height) - 1
        waterlevel = min(height[start], height[end])
        water = 0
        water += min(height[start], height[end]) * (end - start - 1)
        while start < end - 1:
            if height[start] <= height[end]:
                start += 1
                water -= min(waterlevel, height[start])
            else:
                end -= 1
                water -= min(waterlevel, height[end])
            water += max(0, min(height[start], height[end]) - waterlevel) * (end - start - 1)
            waterlevel = max(waterlevel, min(height[start], height[end]))
        print(height[start])
        print(height[end])
        print(waterlevel)
        return water

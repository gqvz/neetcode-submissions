class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while end > start:
            val = numbers[start] + numbers[end]
            if val > target:
                end -= 1
            elif val < target:
                start += 1
            else: return [start+1, end+1]
        return []
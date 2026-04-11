class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        found = []
        for i in range(1, len(nums) - 1):
            start = 0
            end = len(nums) - 1
            target = -nums[i]
            while start < i < end:
                current = nums[start] + nums[end]
                if current > target:
                    end -= 1
                elif current < target:
                    start += 1
                else: 
                    a = sorted([nums[start], nums[end], nums[i]])
                    if a not in found:
                        found.append(a)
                    end -= 1
                    start += 1

        return found

        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return -1
        if target > nums[-1]: return -1
        if target == nums[0]: return 0

        start = 0
        end = len(nums) - 1
        mid = -1
        while (start < end or mid != end) and end > 0:
            mid = (end + start) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                end = mid-1
            else: start = mid+1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[lo] == target: return lo
            if nums[hi] == target: return hi
            if nums[mid] == target: return mid
            if nums[lo] < target < nums[mid]: hi = mid - 1
            elif target < nums[lo] <= nums[mid]: lo = mid + 1
            elif target < nums[mid] <= nums[lo]: hi = mid - 1
            elif nums[mid] <= nums[lo] < target: hi = mid - 1
            elif nums[mid] < target < nums[lo]: lo = mid + 1
            elif nums[lo] < nums[mid] < target: lo = mid + 1

        return -1

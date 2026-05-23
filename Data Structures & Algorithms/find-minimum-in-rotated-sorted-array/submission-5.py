class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        mid = 0
        if len(nums) == 1:
            return nums[0]
        while lo <= hi:
            mid = (lo + hi) >> 1
            if nums[hi] < nums[lo] <= nums[mid]:
                lo = mid+1
            elif nums[mid] <= nums[hi] < nums[lo]:
                hi = mid-1
            elif nums[lo] < nums[mid] < nums[hi]:
                return nums[lo]
            if mid == 0:
                if nums[mid] < nums[mid+1]: return nums[mid]
            if mid == len(nums) - 1:
                if nums[mid] < nums[mid-1]: return nums[mid]
            if nums[mid-1] > nums[mid] < nums[mid+1]:
                break
        return nums[mid]

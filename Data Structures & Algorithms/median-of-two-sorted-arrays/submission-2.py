class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        for i in range(len(nums1) + len(nums2)):
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    result.append(nums1.pop(0))
                else:
                    result.append(nums2.pop(0))
            elif nums1:
                result += nums1
                break
            elif nums2:
                result += nums2
                break
        print(result)
        if len(result) % 2 == 0:
            return (result[len(result) // 2] + result[len(result) // 2 - 1]) / 2
        return result[len(result) // 2]
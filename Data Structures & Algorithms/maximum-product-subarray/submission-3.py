class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur = 1
        m = float("-inf")
        neg = 0
        for num in nums:
            if num == 0: 
                cur = 1
                neg = 0
                continue
            cur *= num
            m = max(m, cur)
            if cur < 0:
                if neg != 0:
                    cur *= neg
                    m = max(m, cur)
                    neg = 0
                else:
                    neg = cur
                    cur = 1
        cur = 1
        neg = 0
        for num in nums[::-1]:
            if num == 0: 
                cur = 1
                neg = 0
                continue
            cur *= num
            m = max(m, cur)
            if cur < 0:
                if neg != 0:
                    cur *= neg
                    m = max(m, cur)
                    neg = 0
                else:
                    neg = cur
                    cur = 1

        return max(m, max(nums))


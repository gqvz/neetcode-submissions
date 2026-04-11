class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num - 1 in m:
                m[num] = False
            else: m[num] = True
        print(m)
        longest = 0
        for (num, f) in m.items():
            if not f: continue
            k = num
            now = 1
            while k + 1 in m:
                now += 1
                k += 1
            if now > longest: longest = now
        return longest
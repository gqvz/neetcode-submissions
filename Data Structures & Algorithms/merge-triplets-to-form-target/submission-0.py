class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        c = [0]*3
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                c[0] = max(c[0], t[0])
                c[1] = max(c[1], t[1])
                c[2] = max(c[2], t[2])
        # print(c)
        return all(c[i]==target[i] for i in [0, 1, 2])

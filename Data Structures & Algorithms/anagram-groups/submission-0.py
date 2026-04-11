import itertools
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            added = False
            for k in d.keys():
                if k == str(sorted(s)):
                    d[k] += [s]
                    added = True
            if not added:
                d[str(sorted(s))] = [s]
        return list(d.values())
from _heapq import heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand) // groupSize
        if n * groupSize != len(hand):
            return False
        groups = [[]]
        hand.sort()
        for h in hand:
            inserted = False
            for g in groups:
                if not g:
                    g.append(h)
                    inserted = True
                    break
                if h - g[-1] == 1 and len(g) < groupSize:
                    g.append(h)
                    inserted = True
                    break

            if not inserted: groups.append([h])
            if len(groups) > n:
                return False
        return True

        
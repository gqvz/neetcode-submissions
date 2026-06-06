from _heapq import heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand) // groupSize
        if n * groupSize != len(hand):
            return False
        hand.sort()
        if groupSize == 1:
            return True
        groups = deque([[hand[0]]])
        cf = 0
        print(hand)
        for i in range(1, len(hand)):
            d = hand[i] - hand[i-1]
            print(groups, hand[i], d)
            if d > 1:
                if len(groups) > 0: return False
                cf = 0
                groups.append([hand[i]])
            elif d == 1:
                cf = 0
                if len(groups) > 0 and hand[i]-groups[0][-1] != 1: return False
                if len(groups) == 0:
                    groups.append([hand[i]])
                else: groups[0].append(hand[i])
                if len(groups[0]) == groupSize:
                    groups.popleft()
                    cf -= 1
            elif d == 0: # d = 0
                cf += 1
                if cf == len(groups):
                    groups.append([hand[i]])
                    continue
                groups[cf].append(hand[i])
                if len(groups[0]) == groupSize:
                    groups.popleft()
                    cf -= 1

            else: raise

        print(groups)
        return len(groups) == 0
                

        
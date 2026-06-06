class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        en = (i for i in range(len(gas)) if gas[i] >= cost[i])
        while True:
            i = next((en), -1)
            if i == -1: return i

            fuel = gas[i]-cost[i]
            idx = (i + 1) % len(gas)
            found = True
            while idx != i:
                fuel += gas[idx]-cost[idx]
                if fuel < 0: 
                    found = False
                idx += 1
                idx %= len(gas)
            if found:
                return i
        return -1

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if len(a) >= 1 and temp > temperatures[a[-1]]:
                for x in range(len(a)-1, -1, -1):
                    if temperatures[a[x]] < temp:
                        result[a[x]] = i - a[x]
                        a.pop()
            a.append(i)

            
        return result


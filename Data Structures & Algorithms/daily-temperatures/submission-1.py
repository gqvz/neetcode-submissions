class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            a.append(i)
            if len(a) > 1 and temp > temperatures[a[-2]]:
                a.pop()
                for x in a[::-1]:
                    if temperatures[x] < temp:
                        result[x] = i - x
                        a.pop()
                a.append(i)

            
        return result


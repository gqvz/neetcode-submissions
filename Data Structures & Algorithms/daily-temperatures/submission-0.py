class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = []
        result = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            a.append(i)
            if len(a) > 1 and temp > temperatures[a[-2]]:
                for x in a[::-1]:
                    if temperatures[x] < temp: result[x] = i - x
                a = list(filter(lambda x: temperatures[x] >= temp, a))
            
        return result


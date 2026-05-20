class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position: 
            return 0
        cars = sorted(zip(position, speed))
        st = [cars[0]]
        for car in cars[1:]:
            last = st[-1]
            if last[1] <= car[1]:
                st.append(car)
                continue
            time_to_end_curr = (target - car[0]) / car[1]
            while st:
                o = st[-1]
                if o[1] <= car[1]: 
                    break
                time_to_catchup = (car[0] - o[0]) / (o[1] - car[1])
                if time_to_catchup <= time_to_end_curr:
                    st.pop()
                else: 
                    break
            st.append(car)

        return len(st)
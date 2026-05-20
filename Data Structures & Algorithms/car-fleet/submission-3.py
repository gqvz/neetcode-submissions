class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1: return 1
        idp = [(i, x, speed[i]) for i, x in enumerate(position)]
        st = []
        idp = sorted(idp, key=lambda x: x[1])
        st.append(idp[0])
        print(idp)
        for car in idp[1:]:
            last = st[-1]
            if last[2] <= car[2]:
                st.append(car)
                continue
            for o in st[::-1]:
                if o[2] <= car[2]: continue
                time_to_end_curr = (target - car[1]) / car[2]
                time_to_catchup = (car[1] - o[1]) / (o[2] - car[2])
                if time_to_catchup <= time_to_end_curr:
                    st.pop(st.index(o))
                else: break
            st.append(car)

        return len(st)

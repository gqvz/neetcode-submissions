class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            match t:
                case '-':
                    b = (st.pop())
                    a = (st.pop())
                    st.append((a - b))
                case '+':
                    b = (st.pop())
                    a = (st.pop())
                    st.append((a + b))
                case '/':
                    b = (st.pop())
                    a = (st.pop())
                    st.append(int(a / b))
                case '*':
                    b = (st.pop())
                    a = (st.pop())
                    st.append((a * b))
                case _:
                    st.append(int(t))
        return st[-1]




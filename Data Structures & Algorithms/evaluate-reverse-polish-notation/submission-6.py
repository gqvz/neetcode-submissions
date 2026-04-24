class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t in "-+/*":
                b = (st.pop())
                a = (st.pop())
                match t:
                    case '-':
                        st.append((a - b))
                    case '+':
                        st.append((a + b))
                    case '/':
                        st.append(int(a / b))
                    case '*':
                        st.append((a * b))
            else:
                st.append(int(t))
        return int(st[-1])



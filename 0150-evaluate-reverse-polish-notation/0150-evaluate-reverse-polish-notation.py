class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n1 = n2 = 0

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                n2 = stack.pop()
                n1 = stack.pop()

                if t=="+":
                    stack.append(n1+n2)

                elif t=="-":
                    stack.append(n1-n2)

                elif t=="*":
                    stack.append(n1*n2)

                elif t=="/":
                    stack.append(int(float(n1)/n2))
                
        return stack.pop()

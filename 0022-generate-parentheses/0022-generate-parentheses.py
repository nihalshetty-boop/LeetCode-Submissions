class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def bt(octr, cctr):
            if octr == cctr == n:
                ans.append("".join(stack))
                return
            
            if octr < n:
                stack.append("(")
                bt(octr+1, cctr)
                stack.pop()
            
            if cctr < octr:
                stack.append(")")
                bt(octr, cctr+1)
                stack.pop()
        
        bt(0, 0)
        return ans
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]

        while matrix:
            #right
            ans += (matrix.pop(0))

            #down
            if matrix and matrix[0]:
                for r in matrix:
                    ans.append(r.pop())
                
            #left
            if matrix:
                ans += (matrix.pop()[::-1])

            #up
            if matrix and matrix[0]:
                for r in matrix[::-1]:
                    ans.append(r.pop(0))
        
        return ans

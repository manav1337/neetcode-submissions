class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(closedN , OpenN):
            if closedN == OpenN == n:
                res.append("".join(stack))
                return
            
            if closedN < OpenN:
                stack.append(")")
                backtrack(closedN + 1, OpenN)
                stack.pop()
            
            if OpenN < n:
                stack.append("(")
                backtrack(closedN , OpenN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
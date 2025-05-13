class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        for i in range(len(s)):
            if s[i] == '(':

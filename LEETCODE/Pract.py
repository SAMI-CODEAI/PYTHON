from panel.interact import empty


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
              s.rstrip(i)
        if s is=='':
            return True
        else:
            return False
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
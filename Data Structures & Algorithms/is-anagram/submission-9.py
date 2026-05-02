class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resultT = {}
        resultS = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            resultS[s[i]] = 1 + resultS.get(s[i], 0)
            resultT[t[i]] = 1 + resultT.get(t[i], 0)
        
        return resultT == resultS
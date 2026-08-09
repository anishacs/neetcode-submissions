class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        if len(s) != len(t):
            return False
        else:
            countS = Counter(s)
            countT = Counter(t)
            if countS == countT:
                return True
            else:
                return False
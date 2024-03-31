# Time: O(n)
# Space: O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        chr_s = {}
        chr_t = {}

        for i in range(len(s)):
            chr_s[s[i]] = 1 + chr_s.get(s[i], 0)
            chr_t[t[i]] = 1 + chr_t.get(t[i], 0)
        
        for i in chr_s:
            if chr_s[i] != chr_t.get(i, 0):
                return False
        return True

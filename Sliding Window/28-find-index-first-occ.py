class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0 
        r = len(needle) - 1
        count = 0
        res = len(haystack) - len(needle)
        while r<len(haystack):
            if haystack[l:r+1] == needle:
                res = min(res, l)
                count+=1
            l+=1
            r+=1
        return res if count!=0 else -1




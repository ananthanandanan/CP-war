class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }
        count = 0
        l=0
        while l < len(s):
            if (l+1)<len(s) and hashMap[s[l]] < hashMap[s[l+1]]:
                count+= (hashMap[s[l+1]] - hashMap[s[l]])
                l+=2
            else:
                count+=hashMap[s[l]]
                l+=1
        return count
            
        
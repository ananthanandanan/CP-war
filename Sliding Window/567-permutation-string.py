"""
The logic is to use a sliding window to check if the current window contains all the characters of the given string.
We can use a hashmap to a list(since we have only 26 characters) to keep track of the characters in the current window.
we can use a "matches" variable to keep track of how many characters match with the desired string. 
If the matches equals 26, we have found our desired permutation.

In the first loop, we just count the first s1.length() characters in s2 and store them in the hashmap. Then take 
an initial matches check between both the hashmaps.

Then in the second loop, we slide the window from s1.length() to s2.length() and check if the matches is 26. So as the right slider
slides, we increment the count of the character at the right slider in the hashmap. If the count of the character at the right slider
is equal to the count of the character in the hashmap of the desired string, we increment the matches. If the count of the character at the right slider
is equal to the count of the character in the hashmap of the desired string + 1, we decrement the matches. This is because we are adding a new character
to the window and if the count was already matched but during the slide, that count is incremented, we need to decrement the matches.

Then we slide the left slider and decrement the count of the character at the left slider in the hashmap. If the count of the character at the left 
slider is equal to the count of the character in the hashmap of the desired string, we increment the matches. If the count of the character at the left slider
is equal to the count of the character in the hashmap of the desired string - 1, we decrement the matches. This is because we are removing a character
from the window and if the count was already matched but during the slide, that count is decremented, we need to decrement the matches.


Time Complexity: O(N)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] +=1
            s2Count[ord(s2[i]) - ord("a")] +=1
        
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches+=1
            else:
                continue
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            ## Check right slider
            index = ord(s2[r]) - ord("a")
            s2Count[index] +=1
            if s1Count[index] == s2Count[index]:
                matches+=1
            elif s1Count[index] + 1 == s2Count[index]:
                matches-=1
            
            ## Check left slider
            
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches+=1
            elif s1Count[index] == s2Count[index] + 1:
                matches-=1
            l+=1
        
        return True if matches==26 else False
            

            

        

        

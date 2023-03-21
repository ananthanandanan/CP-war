"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

We will be using two pointers.

Time Complexity: O(n)

"""

def isPalindrome(s:str):
	l, r = 0, len(s) - 1

	## As long as they don't cross each other
	while l<r:
		while l<r and not alpNum(s[l]):
			l+=1
		while r>l and not alpNum(s[r]):
			r-=1
		if s[l].lower() != s[r].lower():
			return False
		l, r = l+1, r-1
	return True



def alpNum(c):
	return (
		ord('A')<= ord(c) <=ord('Z') or 
		ord('a')<= ord(c) <=ord('z') or
		ord('0')<= ord(c) <=ord('9'))


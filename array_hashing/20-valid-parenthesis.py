def isValid(s: str) -> bool:
    stack = []
    bracketMap = {"(":")", "{":"}", "[":"]"}
    for c in s:
        if c in bracketMap:
                stack.append(c)
        elif not stack or bracketMap[stack.pop()] != c:
                return False
    return not stack
        
            
      

def main():
    s = "()"
    print(isValid(s))


if __name__ == '__main__':
	main()
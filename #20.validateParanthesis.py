class Solution:
    def isValid(self, s: str) -> bool:
        symbols = { "}":-1,"{":1, ")":-2,"(":2, "]":-3,"[":3 }
        stack = []
        
        for i in range(0,len(s)):
            stack.append(s[i])
            print(stack, "1")
            if len(stack) != 1 and symbols[stack[-2]] == -symbols[stack[-1]]:
                stack.pop()
                stack.pop()
                print(stack, "2")
            elif symbols[stack[-1]] < 0:
                print(stack, "3")
                return False
            

        if len(stack) == 0:
            return True
        else:
            return False
        


a = Solution()
b = a.isValid("([])")
print(b)
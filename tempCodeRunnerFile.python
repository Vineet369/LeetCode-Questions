class Solution:
   
    def strStr(self, haystack: str, needle: str) -> int:
        Sum = 0 
        for i in needle:
            Sum += ord(i)
        
        k = 0
        numberedStr = []
        needlelength = len(needle)
        for i in haystack:
            numberedStr.append(ord(i))
        print(numberedStr)
        for i in range(len(numberedStr)):
            print(numberedStr[i:needlelength+i])
            print(sum(numberedStr[i:needlelength+i]))
            if sum(numberedStr[i:needlelength+i]) == Sum:
                for j in range(needlelength):
                    if haystack[i+j] == needle[j]:
                        print(haystack[i+j],needle[j])
                        k += 1
                        print(k,needlelength)
                if k == needlelength:
                    print("returned")
                    return i
                else:
                    k = 0
        return -1 

a = Solution()
b = a.strStr("mississippi", "sipp")
print(b)
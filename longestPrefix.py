class Solution:
    def longestCommonPrefix(self, strs) -> str:
        firstStr = strs[0]
        # print(len(strs(i)))
        
        flag = ""
        for i in range(0,len(strs)):
            strRange = min(len(firstStr),len(strs[i]))
            sameStr = ""
            print(strRange)
            for j in range(strRange):
                if firstStr[j] == strs[i][j]:
                    sameStr = sameStr + firstStr[j]
                    print(sameStr,i)
                else:
                    break
            if len(sameStr) < len(flag) or i==1:
                flag = sameStr
                print(flag)
        return flag
    
a = Solution()
b = a.longestCommonPrefix(["flower","flow","flight"])
print(b, "dsda")
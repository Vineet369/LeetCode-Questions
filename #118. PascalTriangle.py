class Solution:
    def generate(self, numRows: int) :
        pascalT = [[1],[1,1]]
        
        for i in range(2,numRows):
            low = 0
            high = 1
            index = 1
            l = []
            l.append(1)
            l.insert(-1,1)
            for j in range(int(i/2)):
                elem = (pascalT[-1][low]+pascalT[-1][high])
                low += 1
                high += 1
                l.insert(index,elem)
                if i%2 == 0 and index == int(i/2):
                    continue
                else:
                    l.insert(-(index+1),elem)
                index += 1
            pascalT.append(l)
        return pascalT

a = Solution()
b = a.generate(5)
print(b)
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        twos = n//2
        ones = 0
        count = 1
        if n%2 != 0:
            ones = 1
        for i in range(twos-1,-1,-1):
            totalElements = n - twos
            count = count + int(math.factorial(totalElements)/(math.factorial(ones)*math.factorial(twos)))
            twos -= 1
            ones += 2
        return count
    
a = Solution()
b = a.climbStairs(6)
print(b)
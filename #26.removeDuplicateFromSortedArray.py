class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums)==0:
            return 0
        else:    
            k = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                k += 1
                nums[k] = nums[i+1]

        return k
    
a= Solution()
b = a.removeDuplicates([1,1,2])
print(b)
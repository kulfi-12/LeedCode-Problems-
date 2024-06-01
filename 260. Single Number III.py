class Solution:
    def singleNumber(self, nums):
        c=[]
        for i in nums:
            if nums.count(i)==1:
                c.append(i)
        return c

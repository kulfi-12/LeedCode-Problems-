class Solution:
    def scoreOfString(self, s):
        c=0
        for i in range(len(s)-1):
            c+= abs((ord(s[i]))-(ord(s[i+1])))
        return c

  or 

class Solution:
    def singleNumber(self, nums):
        return [i for i in nums if nums.count(i) == 1]

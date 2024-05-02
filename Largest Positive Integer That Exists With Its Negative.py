class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        while nums:
            i=max(nums)
            if -i in nums:
                return i 
            else:
                nums.pop(nums.index(i))
        return -1

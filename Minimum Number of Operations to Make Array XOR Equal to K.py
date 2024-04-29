class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = 0
        for i in nums:
            temp ^= i
        temp ^= k
        return bin(temp).count('1')

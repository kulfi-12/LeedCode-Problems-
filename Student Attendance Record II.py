class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9+7
        arr = [0,0,0,0,0,1]
        for i in range(n):
            arr = [arr[1],arr[2],sum(arr) % mod,arr[4],arr[5],sum(arr[3:]) % mod]
        return sum(arr) % mod

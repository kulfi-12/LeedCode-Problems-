class Solution:
    def countTriplets(self, arr):
        ans=0
        for x in range(len(arr)-1):
            for y in range(x+2,len(arr)+1):
                t=0
                for k in range(x,y):
                    t^=arr[k]
                if t==0:
                    ans+= y-x-1
        return ans

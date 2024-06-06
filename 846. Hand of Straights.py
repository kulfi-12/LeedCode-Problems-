def isNStraightHand(self,hand, groupSize):
    if len(hand) % groupSize != 0:
        return False
    hand.sort()
    from collections import Counter
    count = Counter(hand)
    while count:
        min_val = min(count)
        for i in range(min_val, min_val + groupSize):
            if count[i] == 0:
                return False
            count[i] -= 1
            if count[i] == 0:
                del count[i]
    return True

or 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        k = len(hand) // groupSize
        for i in range(k):
            for j in range(max(hand) - groupSize + 1, max(hand) + 1):
                try:
                    hand.remove(j)
                except:
                    return False
        
        return True

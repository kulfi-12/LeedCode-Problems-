class Solution:
    def numSteps(self, s):
        return len(s) + s.rstrip('0').count('0') + 2 * (s.count('1') != 1) - 1

or


class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        steps = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            steps += 1
        return steps

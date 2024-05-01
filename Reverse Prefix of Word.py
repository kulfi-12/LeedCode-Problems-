class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            i=word.index(ch)+1
            o= word[0:i][::-1]+word[i:]
        else:
            o=word
        return o

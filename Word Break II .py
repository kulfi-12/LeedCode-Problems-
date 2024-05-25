class Solution:
    def wordBreak(self, s, wordDict):
        def recur(s, path):
            if not s:
                out.append(' '.join(path))
                return
            for i in range(1, len(s) + 1):
                w, new_s = s[:i], s[i:]
                if w in wordDict:
                    recur(new_s, path + [w])
        wordDict, out = set(wordDict), []
        recur(s, [])
        return out

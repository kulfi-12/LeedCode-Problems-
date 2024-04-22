class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)
        q = ["0000"]
        lookup = {"0000"}
        depth = 0
        while q:
            next_q = []
            for node in q:
                if node == target: return depth
                if node in dead: continue
                for i in range(4):
                    n = int(node[i])
                    for d in (-1, 1):
                        nn = (n+d) % 10
                        neighbor = node[:i] + str(nn) + node[i+1:]
                        if neighbor not in lookup:
                            lookup.add(neighbor)
                            next_q.append(neighbor)
            q, next_q = next_q, []
            depth += 1
        return -1

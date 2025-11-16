class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != result[j]:
                    return False
                c = start[i]
                if c == 'R' and i > j or c == 'L' and i < j:
                    return False
                i += 1
                j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if result[j] != 'X':
                return False
            j += 1
        return True




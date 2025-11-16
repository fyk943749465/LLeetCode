from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:

        a.sort()
        b.sort()
        i = j = 0
        ans = 2147483647
        while i < len(a) and j < len(b):
            while i < len(a) and j < len(b) and a[i] <= b[j]:
                ans = min(ans, b[j] - a[i])
                if ans == 0:
                    return 0
                i += 1
            while j < len(b) and i < len(a) and b[j] <= a[i]:
                ans = min(ans, a[i] - b[j])
                if ans == 0:
                    return 0
                j += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    x = s.smallestDifference([1,3,15, 11, 2], [23, 127, 235, 19, 8])
    print(x)
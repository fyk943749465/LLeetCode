class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:

        ans = list()
        for v in s:
            if v == 'a':
                if len(ans) > 0 and ans[-1] == 'b':
                    ans.pop()
                else:
                    ans.append(v)
            else:
                if len(ans) > 0 and ans[-1] == 'a':
                    ans.pop()
                else:
                    ans.append(v)
        return len(ans)

if __name__ == '__main__':
    sol = Solution()
    x = sol.minLengthAfterRemovals('ba')
    print(x)
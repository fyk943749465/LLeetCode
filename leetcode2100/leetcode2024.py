class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        ans = left = 0
        tCnt = fCnt = 0
        for i, c in enumerate(answerKey):
            if c == 'T':
                tCnt += 1
            else:
                fCnt += 1

            while fCnt > k and tCnt > k:
                if answerKey[left] == 'T':
                    tCnt -= 1
                else:
                    fCnt -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxConsecutiveAnswers("TTFF", 2)
    print(x)
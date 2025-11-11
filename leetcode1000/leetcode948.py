from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:

        ans = score = 0
        left, right = 0, len(tokens) - 1
        tokens.sort()
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                ans = max(ans, score)
                left += 1
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.bagOfTokensScore([200, 100], 150)
    print(x)
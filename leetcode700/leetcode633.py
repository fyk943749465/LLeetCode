class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        if c == 1:
            return True
        left = 0
        right = min(c//2, 65535)
        while left <= right:
            if left * left + right * right == c:
                return True
            elif left * left + right * right < c:
                left += 1
            else:
                right -= 1
        return False

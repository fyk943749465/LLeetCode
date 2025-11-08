class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        ans = len(s)
        while left < right:
            lefta = s[left]
            rightb = s[right]
            if lefta == rightb:
                while left < len(s) and s[left] == lefta:
                    left += 1
                while right >=0 and s[right] == rightb:
                    right -= 1
            else:
                break
            if left < right:
                ans = min(ans, right - left + 1)
            elif left == right:
                ans = 1
            else:
                ans = 0
        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.minimumLength("aabaaa")
    print(x)

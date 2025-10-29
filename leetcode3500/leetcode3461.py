class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            temp = ''
            for i in range(len(s)-1):
                sum_dig = (int(s[i]) + int(s[i+1]))%10
                temp += str(sum_dig)
            s = temp
        return s[0] == s[1]
if __name__ == '__main__':
    s = "3902"
    solution = Solution()
    print(solution.hasSameDigits(s))

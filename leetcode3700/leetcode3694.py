class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        L=R=U=D=0
        stepMap = {}
        for i, c in enumerate(s):
            if c == 'U':
                U += 1
            elif c == 'D':
                D += 1
            elif c == 'L':
                L += 1
            else:
                R += 1
            # 更新答案
            if i - k + 1 >= 0:
                key = f"{U-D}-{L-R}"
                if key in stepMap:
                    stepMap[key] += 1
                else:
                    stepMap[key] = 1
                # 离开窗口时候，要减去计数
                if s[i-k+1] == 'U':
                    U -= 1
                elif s[i-k+1] == 'D':
                    D -= 1
                elif s[i-k+1] == 'L':
                    L -= 1
                else:
                    R -= 1
        return len(stepMap)

if __name__ == '__main__':
    sol = Solution()
    x = sol.distinctPoints("DURLU", 2)
    print(x)
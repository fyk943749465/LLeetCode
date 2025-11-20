from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        i,j = 0,1
        ans = 0
        while j < len(neededTime):
            if colors[i] == colors[j]:
                if neededTime[i] <= neededTime[j]:
                    ans += neededTime[i]
                    i = j
                else:
                    ans += neededTime[j]
            else:
                i = j
            j += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    x = sol.minCost("abaac", [1,2,3,4,5])
    print(x)
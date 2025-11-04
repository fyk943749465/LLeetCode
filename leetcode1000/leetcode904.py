from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruitMap = {}
        ans = left = 0
        for i, fruit in enumerate(fruits):
            if fruit not in fruitMap:
                fruitMap[fruit] = 1
            else:
                fruitMap[fruit] += 1
            while len(fruitMap) > 2:
                if fruitMap[fruits[left]] == 1:
                    fruitMap.pop(fruits[left])
                else:
                    fruitMap[fruits[left]] -= 1
                left+=1
            ans = max(ans, i - left + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    sol.totalFruit([0,1,2,2])
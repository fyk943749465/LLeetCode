from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]* len(nums)
        flag = True
        s = 0
        for i, v in enumerate(nums):
            if i - k < 0 or i + k > len(nums):
                continue
            if i - k >= 0 and i + k < len(nums):
                if flag:
                    s = sum(nums[0: i + k + 1])
                    flag = False
                else:
                    s = s -  nums[i-k-1] + nums[i+k]
                ans[i] = (int)(s/(2*k+1))
        return ans

    def getAverages2(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]* len(nums)
        s = 0
        for i, v in enumerate(nums):
            s += v
            # 1. 窗口大小
            if i < 2 * k:
                continue
            ans[i-k] = s // (2*k+1)
            # 离开窗口
            s -= nums[i-2 * k]
        return ans

if __name__ == '__main__':
    sol = Solution()
    ans = sol.getAverages([7,4,3,9,1,8,5,2,6], 3)
    print(ans)
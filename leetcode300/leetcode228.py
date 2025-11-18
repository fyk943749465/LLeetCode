from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        pre = ""
        for i, v in enumerate(nums):
            if i == 0:
                pre = str(v)
                j = i
            else:
                if nums[i - 1] + 1 != nums[i]:
                    if i - j > 1:
                        ans.append(pre + '->' + str(nums[i - 1]))
                    else:
                        ans.append(pre)
                    pre = str(v)
                    j = i
                elif i == len(nums) - 1:
                    ans.append(pre + '->' + str(nums[i]))
                    pre = ""
        if pre != "":
            ans.append(str(pre))
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))
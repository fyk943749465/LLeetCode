from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        j = 1
        i = ans = 0
        flag = True
        while j < len(arr):
            if flag:
                i = j - 1
            if arr[j] > arr[j -1]:
                flag = False
                j += 1
            elif i != j-1 and arr[j] < arr[j-1]:
                while j + 1 < len(arr) and arr[j] > arr[j + 1]:
                    j += 1
                ans = max(ans, j - i + 1)
                flag = True
            else:
                j += 1
                flag = True
        return ans


if __name__ == '__main__':
    s = Solution()
    x = s.longestMountain([2,1,4,7,3,2,5])
    print(x)

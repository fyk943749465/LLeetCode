from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        length = len(arr)
        l = list()
        # 在两个数之间插入一个数字，如果两个数相等，插入2
        # 当前数小于前一个数，插入0。否则，插入1
        for i in range(1, length):
            if arr[i] > arr[i - 1]:
                l.append(1)
            elif arr[i] < arr[i - 1]:
                l.append(0)
            else:
                l.append(2)
        # 开始找最长的 1010...或0101...
        i = ans = cnt = 0
        while i < len(l):
            if l[i] == 2:
                i += 1
                cnt = 0
                continue
            if cnt == 0:
                cnt = 1
                pre = l[i]
            else:
                if pre != l[i]:
                    cnt += 1
                else:
                    cnt = 1
                pre = l[i]
            ans = max(ans, cnt)
            i+= 1
        if ans :
            return ans + 1
        else:
            for i in l:
                if i == 0 or i == 1:
                    return 2
            return 1

if __name__ == '__main__':
    solution = Solution()
    x = solution.maxTurbulenceSize([2,0,2,4,2,5,0,1,2,3])
    print(x)
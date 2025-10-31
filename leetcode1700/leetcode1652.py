from typing import List


class Solution:
    # 前缀和
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        if k < 0:
            code.reverse()

        ans = [0] * len(code)
        prefix_total = [0] * 2 * len(code)
        total = 0
        for i in range(2 * len(code)):
            total += code[i % (len(code))]
            prefix_total[i] = total

        for i in range(len(code)):
            ans[i] = prefix_total[i + abs(k)] - prefix_total[i]

        if k < 0:
            ans.reverse()
        return ans

    # TODO: 设计一个滑动窗口
    def decrypt2(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        r = k + 1 if k >0 else n # 第一个窗口的右开断点
        k = abs(k)
        s = sum(code[r-k: r])    # 第一个窗口的元素和

        ans = [0] * len(code)
        for i in range(n):
            ans[i] = s
            s += code[r%n] - code[(r-k)%n]
            r += 1
        return ans
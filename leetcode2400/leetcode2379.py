class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        wnum = blocks.count('W')
        cnt = 0
        for i, v in enumerate(blocks):
            if v == 'W':
                cnt += 1
            # 可以更新答案了
            if i >= k-1:
                wnum = min(wnum, cnt)
                # 离开时候，减去1
                if blocks[i- k + 1] == 'W':
                    cnt -= 1
        return wnum

if __name__ == '__main__':
    sol = Solution()
    x = sol.minimumRecolors(blocks='WWBBBWBBBBBWWBWWWB', k=16)
    print(x)
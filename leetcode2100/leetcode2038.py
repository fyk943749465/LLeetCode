class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        if len(colors) <= 2:
            return False

        i = j = 1
        while True:
            while i < len(colors)-1:
                if colors[i] == colors[i+1] == colors[i-1] and colors[i] == 'A':
                    break
                i += 1
            if i < len(colors)-1 and colors[i] == colors[i+1] == colors[i-1] and colors[i] == 'A':
                i += 1
            else:
                return False
            if i == len(colors):
                return False
            while j < len(colors)-1 :
               if colors[j] == colors[j+1] == colors[j-1] and colors[j] == 'B':
                   break
               else:
                   j += 1
            if j < len(colors) -1 and colors[j] == colors[j + 1] == colors[j - 1] and colors[j] == 'B':
                j += 1
            else:
                return True
            if j == len(colors):
                return True
    # 根据操作手决定：当 Alice 的操作数大于Bob的操作数时候，就获胜了
    def winnerOfGame2(self, colors: str) -> bool:
        freq = [0, 0]
        cur, cnt = 'C', 0
        for c in colors:
            if c != cur:
                cur = c
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    freq[ord(cur) - ord('A')] += 1
        return freq[0] > freq[1]

if __name__ == '__main__':
    sol = Solution()
    x = sol.winnerOfGame('ABBBBBBBAAA')
    print(x)
class Solution:
    def pushDominoes(self, s: str) -> str:
        dominoes = list(s)
        i = 0
        while i < len(dominoes):
            if dominoes[i] == 'L':
                j = i - 1
                while j >= 0 and dominoes[j] == '.':
                    dominoes[j] = 'L'
                    j -= 1
            elif dominoes[i] == 'R':
                i += 1
                j = i
                while i < len(dominoes) and dominoes[i] == '.':
                    i += 1
                if i < len(dominoes):
                    if dominoes[i] == 'R':
                        while j < i:
                            dominoes[j] = 'R'
                            j += 1
                        continue
                    else:
                        k = i - 1
                        while j < k:
                            dominoes[j] = 'R'
                            dominoes[k] = 'L'
                            j += 1
                            k -= 1
                else:
                    while j < len(dominoes):
                        dominoes[j] = 'R'
                        j += 1
            i += 1
        return "".join(dominoes)

if __name__ == '__main__':
    sol = Solution()
    x = sol.pushDominoes("RR.L")
    print(x)


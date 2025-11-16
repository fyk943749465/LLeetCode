class Solution:

    # 双指针经典题目
    def numSub(self, s: str) -> int:
        i = j = 0
        ans = 0
        while j < len(s):
            if s[j] == '0':
                j+=1
                i = j
                continue
            while i <= j and s[i] == '0':
                i += 1
            ans += (j-i+1)
            ans %= 1e9+7
            j += 1
        return int(ans)
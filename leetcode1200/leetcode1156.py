class Solution:
    def maxRepOpt1(self, text: str) -> int:

        cnt = [0] * 26
        for c in text:
            cnt[ord(c) - 97] += 1

        left = 0
        ans = 1
        cnt2 = {}
        for i, c in enumerate(text):
            if c in cnt2:
                cnt2[c] += 1
            else:
                cnt2[c] = 1
            while len(cnt2)>=2:
                if len(cnt2) == 2:
                    flag = False
                    for k, v in cnt2.items():
                        if v == 1:
                            flag = True
                            break;
                    if flag:
                        break;
                    else:
                        if cnt2[text[left]] == 1:
                            cnt2.pop(text[left])
                        else:
                            cnt2[text[left]] -= 1
                        left+= 1
                else:
                    if cnt2[text[left]] == 1:
                        cnt2.pop(text[left])
                    else:
                        cnt2[text[left]] -= 1
                    left += 1
            if len(cnt2) == 2:  # 有两个字符的情况
                for k, v in cnt2.items():
                    if v != 1:
                        if cnt[ord(k)-97] != cnt2[k]:
                            ans = max(ans, i - left + 1)
                        else:
                            ans = max(ans, i - left)
                    else:
                        if cnt[ord(k)-97] > 1:
                            ans = max(ans, 2)
            else:  # 只有一个字符的情况
                ans = max(ans, i - left + 1)

        return ans

if __name__ == '__main__':
    sol = Solution()
    x = sol.maxRepOpt1("abcdef")
    print(x)
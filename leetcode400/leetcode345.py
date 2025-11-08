class Solution:
    def reverseVowels(self, s: str) -> str:
        right = len(s)-1
        left = 0
        ls = []
        for c in s:
            ls.append(c)
        while left < right:
            if ls[left] not in 'aeiouAEIOU':
                left += 1
            if ls[right] not in 'aeiouAEIOU':
                right -= 1
            if left < right and ls[left] in 'aeiouAEIOU' and ls[right] in 'aeiouAEIOU':
                t = ls[left]
                ls[left] = ls[right]
                ls[right] = t
                left += 1
                right -= 1
        return "".join(ls)

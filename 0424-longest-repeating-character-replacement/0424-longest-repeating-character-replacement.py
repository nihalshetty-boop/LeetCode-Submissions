class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ctr = {}
        ans = 0
        l = 0
        maxF = 0

        for r in range(len(s)):
            ctr[s[r]] = 1 + ctr.get(s[r], 0)
            maxF = max(maxF, ctr[s[r]])

            while (r - l + 1) - maxF > k:
                ctr[s[l]] -= 1
                l += 1
            
            ans = max(ans, r - l + 1)

        return ans
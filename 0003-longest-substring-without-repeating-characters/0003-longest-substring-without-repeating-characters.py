class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, r = 0, 1
        max_len = 0

        if s:
            char_set.add(s[l])
            max_len = 1
            
        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                max_len = max(max_len, len(char_set))
                r += 1
            else:
                char_set.remove(s[l])
                l += 1
        
        return max_len

            
            
            
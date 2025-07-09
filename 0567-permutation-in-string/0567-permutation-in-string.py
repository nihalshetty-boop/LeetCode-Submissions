class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cs1 = [0] * 26
        cs2 = [0] * 26
        matches = 0

        for c in range(len(s1)):
            cs1[ord(s1[c]) - ord("a")] += 1
            cs2[ord(s2[c]) - ord("a")] += 1

        for i in range(26):
            matches += (1 if cs1[i] == cs2[i] else 0)
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord("a")
            cs2[idx] += 1

            if cs1[idx] == cs2[idx]:
                matches += 1
            elif cs1[idx] + 1 == cs2[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord("a")
            cs2[idx] -= 1

            if cs1[idx] == cs2[idx]:
                matches += 1
            elif cs1[idx] - 1 == cs2[idx]:
                matches -= 1
            l += 1

        return matches == 26
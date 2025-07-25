class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        ctrT, win = {}, {}
        for c in t:
            ctrT[c] = 1 + ctrT.get(c, 0)

        have, need = 0, len(ctrT)
        res, reslen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c, 0)

            if c in ctrT and win[c] == ctrT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r - l + 1
                
                win[s[l]] -= 1
                if s[l] in ctrT and win[s[l]] < ctrT[s[l]]: 
                    have -= 1
                l += 1

        l, r = res
        return s[l: r+1] if reslen != float("infinity") else ""



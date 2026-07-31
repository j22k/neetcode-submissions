class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t): 
            return ""
        
        # Character frequency maps
        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
            
        # Global minimum tracking configuration
        res, resLen = [-1, -1], float("infinity")
        l = 0
        have, need = 0, len(countT)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            # Increment valid match count
            if c in countT and window[c] == countT[c]:
                have += 1
                
            # Shrink window from the left while conditions match
            while have == need:
                # Update optimal tracking dimensions
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                    
                # Pop the character out from the left boundary
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        start, end = res
        return s[start:end + 1] if resLen != float("infinity") else ""

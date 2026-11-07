class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r=0,0
        countT,state = Counter(t),Counter()
        best = ""
        if len(t)>len(s):
            return ""
        have = 0
        for c in s:
            state[c]+=1

            if state[c]==countT[c]:
                have+=countT.get(c)
            
            while have==len(t):
                if (len(best)>(r-l+1)) or best == "":
                    best = s[l:r+1]
                
                if state[s[l]]==countT[s[l]]:
                    have-=countT[s[l]]
                
                state[s[l]]-=1
                l+=1
            r+=1
        return best

        
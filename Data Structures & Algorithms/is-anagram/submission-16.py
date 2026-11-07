class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #standardize each string using dict of characters and their frequencies and compare
        #early return for two different lengths
        if len(s)!=len(t):
            return False
        
        countsS={}
        countsT={}
        for i in range(len(s)):
            countsS[s[i]] = 1 + countsS.get(s[i],0)
            countsT[t[i]] = 1 + countsT.get(t[i],0)

        return countsS==countsT
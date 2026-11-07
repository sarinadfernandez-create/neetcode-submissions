class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #standardize each string using dict of characters and their frequencies and compare
        #early return for two different lengths
        if len(s)!=len(t):
            return False
        
        countsS={}
        countsT={}
        for i in range(len(s)):
            countsS[ord(s[i])-ord('a')] = countsS.get((ord(s[i])-ord('a')),0)+1
            countsT[ord(t[i])-ord('a')] = countsT.get((ord(t[i])-ord('a')),0)+1

        return countsS==countsT
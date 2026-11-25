class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        # make the counter object
        countT={}
        countS={}

        # iterate through letters to build counter object
        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
        
        print(countT)
        print(countT)
        #compare
        return countT == countS
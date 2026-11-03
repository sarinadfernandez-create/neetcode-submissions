class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        countsSubset = defaultdict(int)
        counterState = defaultdict(int)

        if len(s1)>len(s2):
            return False
        
        if s1==s2:
            return True
        
        for i in range(len(s1)):
            counterState[s2[i]] += 1
            countsSubset[s1[i]] += 1
        
        if counterState == countsSubset:
            return True
        
        print(countsSubset)
        for r in s2[len(s1):]:
            print(counterState)
            counterState[r] += 1
            counterState[s2[l]] -= 1
            if counterState[s2[l]] == 0:
                del counterState[s2[l]]
            l+=1
            if countsSubset == counterState:
                return True
        return False
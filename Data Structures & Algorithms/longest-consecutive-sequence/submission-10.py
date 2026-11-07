class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = 0
        def runLength(start):
            curr = 1
            while start+1 in seen:
                curr+=1
                start+=1
            return curr
        
        for n in nums:
            if n-1 not in seen:
                maximum=max(runLength(n), maximum)

        
        
        return maximum
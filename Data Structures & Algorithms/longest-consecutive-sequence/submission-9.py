class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maximum = 0
        for n in nums:
            curr = 1
            if n-1 not in seen:
                while n+1 in seen:
                    curr+=1
                    n+=1
            maximum = max(curr, maximum)
        return maximum
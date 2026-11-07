class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        nums = sorted(nums)
        curr = 1
        maximum = 0
        for n in nums:
            if n-1 in seen:
                if n not in seen:
                    curr+=1
                    seen.add(n)
            else:
                curr = 1
                seen.add(n)
            maximum = max(curr, maximum)
        return maximum
        
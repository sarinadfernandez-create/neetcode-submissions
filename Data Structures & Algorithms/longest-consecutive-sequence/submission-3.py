class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # complex part is going to be figuring out when to join sets of consecutive numbers
        # trying to figure out how to do this without a billion if statements
        # just gonna start with relatively brute force solution
        # what if I just join at the end?
        # is it worth it to sort? No order to preserve so original doesn't need to be kept, saving some memory
        nums = sorted(nums)
        seen = set()
        best_streak = 0
        state = 0
        print(nums)
        for n in nums:
            if n-1 in seen:
                if n not in seen:
                    state += 1
                    seen.add(n)
            else:
                state = 1
                seen.add(n)
            best_streak = max(state, best_streak)
        return best_streak

        
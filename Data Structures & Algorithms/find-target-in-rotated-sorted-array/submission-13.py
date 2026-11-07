class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            #one side will be sorted and one side contains target
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0]<=target<=nums[mid]:
                    r = mid
                else:
                    l=mid + 1
            else:
                if nums[mid]<=target<=nums[-1]:
                    l = mid + 1
                else:
                    r = mid
                    print("here4")
        if nums[l]==target:
            return l
        return -1
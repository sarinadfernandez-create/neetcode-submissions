class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            #one side will be sorted and one side contains target
            mid = (l+r)//2
            print("start -- mid: "+str(nums[mid])+", right: "+str(nums[r])+", left: "+str(nums[l]))
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0]<=target<=nums[mid]:
                    r = mid
                    print("here1")
                else:
                    l=mid + 1
                    print("here2")
            else:
                if nums[mid]<=target<=nums[-1]:
                    l = mid + 1
                    print("here3")
                else:
                    r = mid
                    print("here4")
            print("end -- mid: "+str(nums[mid])+", right: "+str(nums[r])+", left: "+str(nums[l]))
        if nums[l]==target:
            return l
        return -1
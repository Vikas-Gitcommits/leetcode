class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        sum=0
        m=len(nums)+1
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>=target:
                l=i-j+1
                if m>l:
                    m=l
                sum-=nums[j]
                j+=1
        return m if m!=(len(nums)+1) else 0
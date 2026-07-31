class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        j=0
        s=0
        c=0
        goal=len(nums)-1
        for i in range(0,len(nums)-1):
            s=max(s,i+nums[i])
            if i==c:
                j+=1
                c=s
                if c>=goal:
                    return j

        
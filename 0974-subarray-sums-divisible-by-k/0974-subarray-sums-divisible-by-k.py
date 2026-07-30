class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        sum=0
        count=0
        for i in nums:
            sum+=i
            rem=sum%k
            if rem in d:
                count+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1
        return count

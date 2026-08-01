class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        maarea=0
        while(l<r):
            if h[l]<=h[r]:
                area=h[l]*(r-l)
                l+=1
            else:
                area=h[r]*(r-l)
                r-=1
            maarea=max(maarea,area)
        return maarea
        
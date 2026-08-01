class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        lb=h[l]
        rb=h[r]
        w=0
        while l<r:
            if lb<=rb:
                l+=1
                lb=max(lb,h[l])
                w+=lb-h[l]
            else:
                r-=1
                rb=max(rb,h[r])
                w+=rb-h[r]
        return w
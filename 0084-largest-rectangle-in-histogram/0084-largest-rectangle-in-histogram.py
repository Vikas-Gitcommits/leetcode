class Solution:
    def largestRectangleArea(self, l: List[int]) -> int:
        ans1=[len(l)]*len(l)
        st=[]
        maxarea=0
        for i in range(len(l)-1,-1,-1):
            while st and l[i]<=l[st[-1]]:
                st.pop()
            if st:
                ans1[i]=st[-1]
            st.append(i)
        st=[]
        ans2=[-1]*len(l)
        for i in range(0,len(l)):
            while st and l[i]<=l[st[-1]]:
                st.pop()
            if st:
                ans2[i]=st[-1]
            st.append(i)
        for i in range(len(l)):
            area=l[i]*(ans1[i]-ans2[i]-1)
            maxarea=max(area,maxarea)
        return maxarea

        
                            
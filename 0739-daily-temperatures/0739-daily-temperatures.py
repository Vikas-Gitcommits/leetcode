class Solution:
    def dailyTemperatures(self,t: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(t)
        for i in range(len(t)-1,-1,-1):
            while st and t[i]>=t[st[-1]]:
                st.pop()
            if st:
                ans[i]=st[-1]-i
            st.append(i)
        return ans
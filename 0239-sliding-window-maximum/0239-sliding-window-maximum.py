class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        st=deque()
        ans=[]
        for i in range(len(nums)):
            if st and st[0]<=i-k:
                st.popleft()
            while st and nums[i]>nums[st[-1]]:
                st.pop()
            st.append(i)
            if i>=k-1:
                ans.append(nums[st[0]])
        return ans
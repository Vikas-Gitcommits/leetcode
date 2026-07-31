class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gassum=sum(gas)
        costsum=sum(cost)
        if costsum>gassum:
            return -1
        gassum=0
        costsum=0
        index=0
        for i in range (len(gas)):
            gassum+=gas[i]
            costsum+=cost[i]
            if gassum<costsum:
                gassum=0
                costsum=0
                index=i+1
        return index

        
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cg = 0
        s = 0
        for i in range(len(gas)):
            cg += gas[i] - cost[i]
            if cg < 0:
                cg = 0
                s = i + 1
        return s
        

        
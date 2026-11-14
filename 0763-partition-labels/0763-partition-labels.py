class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        n = len(s)
        ans = []
        start = 0
        end = 0
        d = {}
        for i in range(n):
            d[s[i]] = i
        for i in range(n):
            end = max(end,d[s[i]])
            if i == end:
                ans.append(end-start+1)
                start = i+1
        return ans


class Solution:
    def maxDepth(self, s: str) -> int:
        m=0;ctr=0
        for i in s:
            if i=="(" :
                ctr+=1
                if m<ctr:
                    m=ctr
            if i==")":
                ctr-=1
        return m
        
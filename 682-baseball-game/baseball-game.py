class Solution:
    def calPoints(self, o: List[str]) -> int:
        i = 0
        l = []
        p = []
        while i<len(o):
            if o[i]!= "C" and o[i]!= "D" and o[i]!= "+":
                l.append(int(o[i]))
                # print(l)
            elif o[i]=="C":
                l.remove(l[-1])
                # print(l)
            elif o[i] == "D":
                l.append(l[-1]*2)
                # print(l)
            elif o[i] == "+":
                l.append(l[-1] + l[-2])
                # print(l)
            i+=1
        return (sum(l))
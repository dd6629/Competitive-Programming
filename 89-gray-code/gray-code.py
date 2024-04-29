class Solution:
    def grayCode(self, n: int) -> List[int]:
        lst = []
        for i in range(2**n):
            gray_code = i ^ (i >> 1)
            lst.append(gray_code)
        return lst
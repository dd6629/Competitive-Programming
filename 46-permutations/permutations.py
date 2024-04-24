class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        def dfs(path, numbers):
            if (len(path) == l):
                res.append(path)
                return
            for i in numbers:
                tmp = []
                for x in numbers:
                    tmp.append(x)
                tmp.remove(i)
                dfs(path+[i], tmp)
        dfs([], nums)
        return res
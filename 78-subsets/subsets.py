class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = len(nums)
        def subset(idx, path):
            res.append(path)
            for i in range(idx, l):
                subset(i+1, path + [nums[i]])
        subset(0, [])
        return res

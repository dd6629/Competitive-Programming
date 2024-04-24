class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, path + [candidates[i]], target - candidates[i])
        candidates.sort()
        result = []
        backtrack(0, [], target)
        return result
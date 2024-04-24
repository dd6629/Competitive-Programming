class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i+1, path + [candidates[i]], target - candidates[i])
        candidates.sort()
        result = []
        backtrack(0, [], target)
        result = [list(x) for x in set(tuple(sorted(x)) for x in result)]
        return result
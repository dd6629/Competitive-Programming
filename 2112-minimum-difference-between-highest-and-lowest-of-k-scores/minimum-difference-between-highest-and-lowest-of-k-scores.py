class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1 or k == 0:
            return 0
        nums.sort()
        windowSize = k
        slidingWindowCount = len(nums)-windowSize + 1
        index = 0
        minimum = sys.maxsize
        while slidingWindowCount > 0:
            tmp = nums[index:windowSize+index]
            minimum_tmp = tmp[-1] - tmp[0]
            if minimum_tmp < minimum:
                minimum = minimum_tmp
            index+=1
            slidingWindowCount-=1
        return minimum
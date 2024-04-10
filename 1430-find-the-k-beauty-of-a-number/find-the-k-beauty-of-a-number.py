class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        num_str = str(num)
        for i in range(len(num_str) - k + 1):
            sub_str = num_str[i:i+k]
            sub_num = int(sub_str)
            if sub_num != 0 and num % sub_num == 0:
                count += 1
        return count

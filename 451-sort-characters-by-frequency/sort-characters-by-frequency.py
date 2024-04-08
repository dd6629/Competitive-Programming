class Solution:
    def frequencySort(self, s: str) -> str:
        frequency_map = {}
        for char in s:
            frequency_map[char] = frequency_map.get(char, 0) + 1
        sorted_characters = sorted(frequency_map, key=lambda x: frequency_map[x], reverse=True)
        sorted_string = ''.join(char * frequency_map[char] for char in sorted_characters)
        return sorted_string

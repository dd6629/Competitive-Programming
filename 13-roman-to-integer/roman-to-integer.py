class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Initialize the total value
        total = 0
    
    # Iterate through the Roman numeral from left to right
        for i in range(len(s)):
        # If the current numeral is smaller than the next one, subtract its value
            if i < len(s) - 1 and roman_to_int_dict[s[i]] < roman_to_int_dict[s[i + 1]]:
                total -= roman_to_int_dict[s[i]]
            else:
                total += roman_to_int_dict[s[i]]
    
        return total
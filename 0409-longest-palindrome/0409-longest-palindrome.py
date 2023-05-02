class Solution:
    def longestPalindrome(self, s: str) -> int:
        c_map = {}
        for c in s:
            if(c in c_map):
                c_map[c] += 1
            else:
                c_map[c] = 1
        
        max_palindrome_len = 0
        for c in c_map:
            max_palindrome_len += (c_map[c] - c_map[c]%2)
            
        if(max_palindrome_len < len(s)):
            max_palindrome_len += 1
        
        return max_palindrome_len
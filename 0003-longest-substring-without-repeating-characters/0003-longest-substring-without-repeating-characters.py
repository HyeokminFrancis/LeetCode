class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        max_len = 0
        for idx, char in enumerate(s):
            if(char in char_map and char_map[char]+1>left):
                left = char_map[char]+1 
            char_map[char] = idx
            max_len = max(max_len, idx-left+1)
        return max_len
            
                
        
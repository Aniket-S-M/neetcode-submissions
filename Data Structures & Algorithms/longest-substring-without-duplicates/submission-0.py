class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()  # Keeps track of characters in our current window
        l = 0         # Left boundary of the window
        max_len = 0   # Stores our record length
        
        for r in range(len(s)):
            # If the current character is already in our window, 
            # shrink the window from the left until the duplicate is gone.
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            # Add the new character to our window set
            seen.add(s[r])
            
            # Update our maximum length
            max_len = max(max_len, r - l + 1)
            
        return max_len
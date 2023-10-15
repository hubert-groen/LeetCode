class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        substring = []
        record = 0
        current_count = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.pop(0)
                current_count -= 1

            else:
                substring.append(s[i])
                current_count += 1
            
            record = max(current_count, record)

        return record
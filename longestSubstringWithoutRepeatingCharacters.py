class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        largest = 0
        string = ""
        right = 0
        left = 0
        for char in s:
            if not char in string:
                string = string + char
                right += 1
                largest = max(largest,right-left)
            else:
                while char in string:
                    left += 1
                    string = string.replace(string[0],"")
                string = string + char
                left -= 1
        return largest



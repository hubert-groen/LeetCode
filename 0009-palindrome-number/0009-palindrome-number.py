class Solution:
    def isPalindrome(self, x: int) -> bool:

        reversed_str = ''

        for i in str(x):
            reversed_str = i + reversed_str

        if str(x) == reversed_str:
            return True
        else:
            return False
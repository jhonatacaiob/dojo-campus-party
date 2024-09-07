class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        x2 = 0
        result = False
        while num >= 1:
            x2 = x2 * 10 + num%10
            num = num // 10
        if x2 == x:
            result = True
        return result
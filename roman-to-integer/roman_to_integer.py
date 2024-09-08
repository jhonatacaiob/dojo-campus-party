class Solution:
    def romanToInt(self, s: str) -> int:
        algarismo = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000,
            }

        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and algarismo[s[i]] < algarismo[s[i + 1]]:
                ans -= algarismo[s[i]]
            else:
                ans += algarismo[s[i]] 

        return ans


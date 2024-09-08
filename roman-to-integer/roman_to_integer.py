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
        s = s[::-1]
        a = 0
        u = 0
        for i in s:
            if algarismo[i] < u:
                a -= algarismo[i]
            else:
                a += algarismo[i]
            u = algarismo[i]
        return a


    
from pytest import fixture

from roman_to_integer import Solution

@fixture
def solution():
    return Solution()

# Exemplo 1:

# Entrada: s = "III"
# Saída: 3
# Explicação: III = 3.

# Exemplo 2:

# Entrada: s = "LVIII"
# Saída: 58
# Explicação: L = 50, V= 5, III = 3.

# Exemplo 3:

# Entrada: s = "MCMXCIV"
# Saída: 1994
# Explicação: M = 1000, CM = 900, XC = 90 e IV = 4.

def test_deve_retornar_3_quando_input_III(solution):
    assert solution.romanToInt('III') == 3


def test_deve_retornar_58_quando_input_LVIII(solution):
    assert solution.romanToInt('LVIII') == 58


def test_deve_retornar_1994_quando_input_MCMXCIV(solution):
    assert solution.romanToInt('MCMXCIV') == 1994
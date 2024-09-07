from pytest import fixture

from palindrome import Solution

@fixture
def solution():
    return Solution()


def test_deve_retornar_true_quando_input_121(solution):
    assert solution.isPalindrome(121) is True

def test_deve_retornar_false_quando_input_121_negativo(solution):
    assert solution.isPalindrome(-121) is False

def test_deve_retornar_false_quando_input_10(solution):
    assert solution.isPalindrome(10) is False
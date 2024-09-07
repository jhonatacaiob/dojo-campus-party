from adding_two_numbers import Solution, list_to_linkedlist
from pytest import fixture


@fixture
def solution():
    s = Solution()
    return s

def test_some(solution):
    esperado = list_to_linkedlist([7, 0, 8])
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    assert solution.addTwoNumbers(l1, l2) == esperado

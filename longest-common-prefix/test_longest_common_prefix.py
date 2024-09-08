from pytest import fixture

from longest_common_prefix import Solution


@fixture
def solution():
    return Solution()


def test_exemplo(solution):
    assert True


def test_esperado_prefixo_comum(solution):
    resultado = solution.longestCommonPrefix(['ator', 'amigo'])
    assert resultado == 'a'


def test_esperado_prefixo_comum1(solution):
    resultado = solution.longestCommonPrefix(
        ['laranja', 'abacate', 'pessego', 'limao']
    )
    assert resultado == ''


def test_esperado_prefixo_comum2(solution):
    resultado = solution.longestCommonPrefix(['flower', 'flow', 'flight'])
    assert resultado == 'fl'


def test_esperado_prefixo_comum3(solution):
    resultado = solution.longestCommonPrefix(
        ['carrodecorrida', 'carrodemão', 'carro']
    )
    assert resultado == 'carro'


def test_esperado_prefixo_comum4(solution):
    resultado = solution.longestCommonPrefix(
        ['carrodecorrida', 'carrodemão', 'carro', 'carrinho', 'carrão', 'c']
    )
    assert resultado == 'c'


def test_esperado_prefixo_comum5(solution):
    resultado = solution.longestCommonPrefix(
        ['c', 'carrodemão', 'carro', 'carrinho', 'carrão']
    )
    assert resultado == 'c'


def test_esperado_prefixo_comum6(solution):
    resultado = solution.longestCommonPrefix(['cola'])
    assert resultado == 'cola'


def test_esperado_prefixo_comum7(solution):
    resultado = solution.longestCommonPrefix(['', 'teste', 'tela'])
    assert resultado == ''


def test_esperado_prefixo_comum8(solution):
    resultado = solution.longestCommonPrefix(['cir', 'car'])
    assert resultado == 'c'

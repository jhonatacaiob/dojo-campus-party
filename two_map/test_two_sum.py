from two_sum import two_sum


def test_deve_retornar_0_1_quando_lista_2_7_11_15_target_9():
    res = two_sum([2, 7, 11, 15], 9)
    assert res == (0, 1)


def test_deve_retornar_1_2_quando_lista_3_2_4_target_6():
    res = two_sum([3, 2, 4], 6)
    assert res == (1, 2)


def test_deve_retornar_0_1_quando_lista_3_3_target_6():
    res = two_sum([3, 3], 6)
    assert res == (0, 1)


def test_deve_retornar_2_3_quando_lista_1_2_3_4_target_6():
    res = two_sum([1, 3, 2, 4], 6)
    assert res == (2, 3)

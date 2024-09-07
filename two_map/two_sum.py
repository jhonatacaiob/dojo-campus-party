def two_sum(nums, target):
    dic_valores = {}

    for posicao, valor in enumerate(nums):
        dic_valores[valor] = posicao

    for posicao, valor in enumerate(nums):
        teste = target - valor
        if dic_valores.get(teste, False):
            if posicao == dic_valores[teste]:
                continue
            return (posicao, dic_valores[teste])

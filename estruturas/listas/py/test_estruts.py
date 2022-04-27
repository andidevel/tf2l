from check_parenteses import check_parenteses

def test_check_parenteses():
    test_cases = {
        "(())": True,
        "()()(()())": True,
        "())": False,
        ")(": False,
        "f(x) = ((x+2)/3)*4": True,
    }

    for k in test_cases:
        got = check_parenteses(k)
        assert got == test_cases[k], f'[{k}] Esperado {test_cases[k]}, retornado {got}'

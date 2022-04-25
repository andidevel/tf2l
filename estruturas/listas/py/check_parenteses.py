test_cases = {
    "(())": True,
    "()()(()())": True,
    "())": False,
    ")(": False,
    "f(x) = ((x+2)/3)*4": True,
}

def check_parenteses(s):
    pilha = []
    for i in s:
        if i == '(':
            pilha.append(1)
        elif i == ')':
            if len(pilha) == 0:
                return False
            pilha.pop()
    return len(pilha) == 0


if __name__ == '__main__':
    print('Testando....')
    for k in test_cases:
        got = check_parenteses(k)
        if got != test_cases[k]:
            print(f'[{k}] Esperado {test_cases[k]}, retornado {got}')
    print('Testes terminados.')
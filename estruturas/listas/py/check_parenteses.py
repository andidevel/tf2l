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

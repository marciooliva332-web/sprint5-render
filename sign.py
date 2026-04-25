# criando a função sign()
def sign(x):
    """Retorna o sinal de número."""
    if x == None:
        return None
    if x < 0:
        return -1
    return 1

# testando a função sign()
def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None
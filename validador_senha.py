# validador de senhas
# 3 < senha < 20
# alfanumerica

MIN_SENHA = 4
MAX_SENHA = 19


def validar(senha):
    if validar_tamanho(senha) and validar_caracteres(senha):
        return 'VALID'
    return 'INVALID'
    

def validar_tamanho(senha):
    if not MIN_SENHA <= len(senha) <= MAX_SENHA:
        return False
    return True

def validar_caracteres(senha):
    if not senha.isalnum():
        return False
    if not any(map(str.isalpha, senha)):
        return False
    if not any(map(str.isdigit, senha)):
        return False
    return True
    
    
if __name__ == '__main__':
    assert validar('Senha123') == 'VALID'
    assert validar('Senha123!') == 'INVALID'
    assert validar('123') == 'INVALID'
    assert validar('SenhaMuitoLonga123456') == 'INVALID'
    assert validar('SenhaTextual') == 'INVALID'
    assert validar('1234') == 'INVALID'
    

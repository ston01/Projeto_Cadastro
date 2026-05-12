menuprincipal = 'MENU PRINCIPAL'
largura = 75


def menu_principal():
    print('='*largura)
    print(menuprincipal.center(largura))
    print('='*largura)
    print(' [ 1 ] - Ver pessoas cadastradas')
    print(' [ 2 ] - Cadastrar nova pessoa')
    print(' [ 3 ] - Pesquisar cadastro')
    print(' [ 4 ] - Deletar cadastro')
    print(' [ 5 ] - Atualizar cadastro')
    print(' [ 6 ] - Sair do programa')
    print('='*largura)


def cabeçalho(msg, larg=75):
    print('-'*larg)
    print(f'{msg.center(larg)}')
    print('-'*larg)
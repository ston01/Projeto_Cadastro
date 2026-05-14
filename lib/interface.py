menuprincipal = '\033[1mMENU PRINCIPAL\033[0m'
largura = 82


def menu_principal():
    print('='*largura)
    print(menuprincipal.center(largura))
    print('='*largura)
    print(' [ 1 ] - Listar cadastros')
    print(' [ 2 ] - Pesquisar cadastro')
    print(' [ 3 ] - Novo cadastro')
    print(' [ 4 ] - Atualizar cadastro')
    print(' [ 5 ] - Deletar cadastro')
    print(' [ 6 ] - Exportar para excel')
    print(' [ 7 ] - Sair do programa')
    print('='*largura)


def cabeçalho(msg, larg=82):
    print('-'*larg)
    print(f'{msg.center(larg)}')
    print('-'*larg)
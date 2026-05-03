menu_principal = 'MENU PRINCIPAL'
largura = 40



def MenuPrincipal():
    print('='*largura)
    print(menu_principal.center(largura))
    print('='*40)
    print(' [ 1 ] - Ver pessoas cadastradas')
    print(' [ 2 ] - Cadastrar nova pessoa')
    print(' [ 3 ] - Sair do sistema')
    print('='*40)


def Opção(msg, larg=40):
    print('-'*larg)
    print(f'{msg.center(larg)}')
    print('-'*larg)
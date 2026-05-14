import os
from lib.validar import validar_int, enter_continuar
from lib.banco import criar_tabela, exportar_para_excel
from lib.interface import menu_principal
from lib import menus
criar_tabela()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    menu_principal()
    escolha = validar_int('Opção escolhida: ')
    if escolha == 1:
        menus.listar_cadastros()
    elif escolha == 2:
        menus.pesquisar_cadastro()
    elif escolha == 3:
        menus.novo_cadastro()
    elif escolha == 4:
        menus.atualizar_cadastro()
    elif escolha == 5:
        menus.deletar_cadastro()
    elif escolha == 6:
        exportar_para_excel() 
    elif escolha == 7:
        menus.encerrar_programa()
    else:
        print('\033[31mERRO: Digite uma opção válida!\033[0m')
    enter_continuar()
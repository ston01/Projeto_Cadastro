from lib.interface import *
from lib.validar import *
from lib.banco import *
geral = []
cadastros = {}
criar_tabela()
while True:
    menu_principal()
    escolha = validar_int('Opção escolhida: ')
    if escolha == 1:
        cabeçalho('OPÇÃO 1')
        pessoas = listar_usuarios()
        for pessoa in pessoas:
            print(f"{pessoa['nome']:<15} | {pessoa['idade']:<3} anos | {pessoa['email']:<30} | {pessoa['celular']}")
    elif escolha == 2:
        cabeçalho('OPÇÃO 2')
        cadastros['Nome'] = validar_str('Nome: ')
        cadastros['Idade'] = validar_int('Idade: ')
        cadastros['Email'] = validar_email('Email: ')
        cadastros['Celular'] = validar_celular('Celular: ')
        inserir_usuario(cadastros['Nome'], cadastros['Idade'], cadastros['Email'], cadastros['Celular'])
    elif escolha == 3:
        cabeçalho('Saindo do programa... Até breve!')
        break
    else:
        print('ERRO: Digite uma opção válida!')
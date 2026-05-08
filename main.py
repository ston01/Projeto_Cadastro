from lib.interface import *
from lib.validar import *
from lib.banco import *
geral = []
cadastros = {}
criar_tabela()
while True:
    menuprincipal()
    escolha = leiaInt('Opção escolhida: ')
    if escolha == 1:
        cabeçalho('OPÇÃO 1')
        pessoas = listar_usuarios()
        for pessoa in pessoas:
            print(f"{pessoa['nome']:.<30}{pessoa['idade']} anos")
    elif escolha == 2:
        cabeçalho('OPÇÃO 2')
        cadastros['Nome'] = leiaStr('Nome: ')
        cadastros['Idade'] = leiaInt('Idade: ')
        inserir_usuario(cadastros['Nome'], cadastros['Idade'])
    elif escolha == 3:
        cabeçalho('Saindo do programa... Até breve!')
        break
    else:
        print('ERRO: Digite uma opção válida!')
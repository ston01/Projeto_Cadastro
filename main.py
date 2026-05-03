from lib.interface import MenuPrincipal, Opção
from lib.dado import leiaInt, leiaStr
geral = []
cadastros = {}
while True:
    MenuPrincipal()
    escolha = leiaInt('Opção escolhida: ')
    if escolha == 1:
        Opção('OPÇÃO 1')
        for pessoa in geral:
            print(f'{pessoa['Nome']} \t {pessoa['Idade']} anos')
    elif escolha == 2:
        Opção('OPÇÃO 2')
        cadastros['Nome'] = leiaStr('Nome: ')
        cadastros['Idade'] = leiaInt('Idade: ')
        geral.append(cadastros.copy())
    elif escolha == 3:
        Opção('Saindo do programa... Até breve!')
        break
    else:
        print('ERRO: Digite uma opção válida!')
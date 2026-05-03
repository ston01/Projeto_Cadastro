from lib.interface import MenuPrincipal, Opção
geral = []
cadastros = {}
while True:
    MenuPrincipal()
    escolha = int(input('Opção escolhida: '))
    if escolha == 1:
        for pessoa in geral:
            Opção('OPÇÃO 1')
            print(f'{pessoa['Nome']} \t {pessoa['Idade']} anos')
    if escolha == 2:
        Opção('OPÇÃO 2')
        cadastros['Nome'] = str(input('Nome: '))
        cadastros['Idade'] = int(input('Idade: '))
        geral.append(cadastros.copy())
    if escolha == 3:
        Opção('Saindo do programa... Até breve!')
        break
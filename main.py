from lib.interface import MenuPrincipal
geral = []
cadastros = {}
while True:
    MenuPrincipal()
    cadastros['Nome'] = str(input('Nome: '))
    cadastros['Idade'] = int(input('Idade: '))
    geral.append(cadastros.copy())
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
            print(f"{pessoa['id']:<3} | {pessoa['nome']:<15} | {pessoa['idade']:<3} anos | {pessoa['email']:<30} | {pessoa['celular']}")
    elif escolha == 2:
        cabeçalho('OPÇÃO 2')
        cadastros['nome'] = validar_str('Nome: ')
        cadastros['idade'] = validar_int('Idade: ')
        cadastros['email'] = validar_email('Email: ')
        cadastros['celular'] = validar_celular('Celular: ')
        inserir_usuario(cadastros['nome'], cadastros['idade'], cadastros['email'], cadastros['celular'])
    elif escolha == 3:
        cabeçalho('OPÇÃO 3')
        nome_busca = validar_str('Digite o nome ou parte dele: ')
        resultados = pesquisar_usuario(nome_busca)
        if resultados:
            for pessoa in resultados:
                print(f"{pessoa['id']:<3} | {pessoa['nome']:<15} | {pessoa['idade']:<3} anos | {pessoa['email']:<30} | {pessoa['celular']}")
        else:
            print(f'Não encontramos ninguém com o nome "{nome_busca}"')
    elif escolha == 4:
        cabeçalho('Saindo do programa... Até breve!')
        break
    else:
        print('ERRO: Digite uma opção válida!')
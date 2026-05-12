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
        cabeçalho('CADASTROS')
        pessoas = listar_usuarios()
        for pessoa in pessoas:
            print(f"{pessoa['id']:<3} | {pessoa['nome']:<15} | {pessoa['idade']:<3} anos | {pessoa['email']:<30} | {pessoa['celular']}")
    elif escolha == 2:
        cabeçalho('PESQUISAR CADASTRO')
        nome_busca = validar_str('Digite o nome ou parte dele: ')
        resultados = pesquisar_usuario(nome_busca)
        if resultados:
            for pessoa in resultados:
                print(f"{pessoa['id']:<3} | {pessoa['nome']:<15} | {pessoa['idade']:<3} anos | {pessoa['email']:<30} | {pessoa['celular']}")
        else:
            print(f'Não encontramos ninguém com o nome "{nome_busca}"')
    elif escolha == 3:
        cabeçalho('NOVO CADASTRO')
        cadastros['nome'] = validar_str('Nome: ')
        cadastros['idade'] = validar_int('Idade: ')
        cadastros['email'] = validar_email('Email: ')
        cadastros['celular'] = validar_celular('Celular: ')
        inserir_usuario(cadastros['nome'], cadastros['idade'], cadastros['email'], cadastros['celular'])
    elif escolha == 4:
        cabeçalho('ATUALIZAR CADASTRO')
        id_edit = validar_int('Digite o ID: ')
        usuario = buscar_usuario(id_edit)
        if usuario:
            print(f"Usuário encontrado! (Pressione ENTER para manter o valor atual)")
            novo_nome = input(f"Nome [{usuario[1]}]: ").strip() or usuario[1]
            nova_idade = input(f"Idade [{usuario[2]}]: ") or usuario[2]
            novo_email = input(f"Email [{usuario[3]}]: ").strip() or usuario[3]
            novo_celular = input(f"Celular [{usuario[4]}]: ").strip() or usuario[4]
            atualizar_usuario(id_edit, novo_nome, nova_idade, novo_email, novo_celular)
        else:
            print('ID não encontrado.')
    elif escolha == 5:
        cabeçalho('DELETAR CADASTRO')
        id_excluir = validar_int('Digite o ID do usuário que deseja remover: ')
        certeza = str(input(f'Tem certeza que deseja apagar o ID {id_excluir}? [S/N]: ')).upper().strip()
        if certeza == 'S':
            deletar_usuario(id_excluir)
            print(f'Usuário {id_excluir} removido com sucesso!')
        else:
            print('Operação cancelada.')
    elif escolha == 6:
        exportar_para_excel() 
    elif escolha == 7:
        cabeçalho('Saindo do programa... Até breve!')
        break
    else:
        print('ERRO: Digite uma opção válida!')
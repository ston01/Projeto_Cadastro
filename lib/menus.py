from lib import banco
from lib.interface import cabeçalho
from lib import validar

def listar_cadastros():
    cabeçalho('CADASTROS')
    pessoas = banco.listar_usuarios()
    for pessoa in pessoas:
        print(f" {pessoa['id']:<3} | {pessoa['nome']:<15} | {pessoa['idade']:<3}anos | {pessoa['email']:<30} | {pessoa['celular']}")


def pesquisar_cadastro():
    cabeçalho('PESQUISAR CADASTRO')
    nome_busca = validar.validar_str('Digite o nome ou parte dele: ')
    resultados = banco.pesquisar_usuario(nome_busca)
    if resultados:
        for pessoa in resultados:
            print(f" {pessoa['id']:<3} | {pessoa['nome']:<15} | {pessoa['idade']:<3} anos | {pessoa['email']:<30} | {pessoa['celular']}")
    else:
        print(f'Não encontramos ninguém com o nome "{nome_busca}"')


def novo_cadastro():
    cabeçalho('NOVO CADASTRO')
    nome = validar.validar_str('Nome: ')
    idade = validar.validar_int('Idade: ')
    email = validar.validar_email('Email: ')
    celular = validar.validar_celular('Celular: ')
    banco.inserir_usuario(nome, idade, email, celular)


def atualizar_cadastro():
    cabeçalho('ATUALIZAR CADASTRO')
    id_edit = validar.validar_int('Digite o ID: ')
    usuario = banco.buscar_usuario(id_edit)
    if usuario:
        print(f"Usuário encontrado! (Pressione ENTER para manter o valor atual)")
        novo_nome = validar.validar_str(f"Nome [{usuario[1]}]: ", False).strip() or usuario[1]
        nova_idade = validar.validar_int(f"Idade [{usuario[2]}]: ", False) or usuario[2]
        novo_email = validar.validar_email(f"Email [{usuario[3]}]: ", False).strip() or usuario[3]
        novo_celular = validar.validar_celular(f"Celular [{usuario[4]}]: ", False).strip() or usuario[4]
        banco.atualizar_usuario(id_edit, novo_nome, nova_idade, novo_email, novo_celular)
    else:
        print('ID não encontrado.')


def deletar_cadastro():
    cabeçalho('DELETAR CADASTRO')
    id_excluir = validar.validar_int('Digite o ID do usuário que deseja remover: ')
    certeza = str(input(f'Tem certeza que deseja apagar o ID {id_excluir}? [S/N]: ')).upper().strip()
    if certeza == 'S':
        banco.deletar_usuario(id_excluir)
        print(f'Usuário {id_excluir} removido com sucesso!')
    else:
        print('Operação cancelada.')


def encerrar_programa():
    cabeçalho('Saindo do programa... Até breve!')
    exit()
def leiaStr(msg):
    while True:
        try:
            string = str(input(msg)).strip()
            if string == '':
                print('ERRO: O campo não pode ficar vazio!')
                continue
        except(KeyboardInterrupt):
            print('Usuário preferiu não digitar.')
            return '<desconhecido>'
        return string


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido!')
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar.')
            return 0
        else:
            return valor
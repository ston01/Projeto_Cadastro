def validar_str(msg):
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


def validar_int(msg):
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
        

def validar_email(msg):
    while True:
        try:
            email = str(input(msg)).strip().lower()
            if email == '':
                print('ERRO: O campo e-mail não pode ficar vazio!')
                continue
            if '@' not in email or '.' not in email:
                print('ERRO: Digite um e-mail válido (exemplo@dominio.com)!')
                continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o e-mail.')
            return '<desconhecido>'
        return email
    

def validar_celular(msg):
    while True:
        try:
            entrada = str(input(msg)).strip()
            apenas_numeros = "".join(char for char in entrada if char.isdigit())
            if apenas_numeros == '':
                print('ERRO: O campo celular não pode ficar vazio!')
                continue
            if len(apenas_numeros) != 11:
                print('ERRO: O celular deve ter 11 dígitos (DDD + número)!')
                continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o celular.')
            return '00000000000'
        return apenas_numeros
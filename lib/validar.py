def validar_str(msg, obrigatorio=True):
    while True:
        try:
            string = str(input(msg)).strip()
            if not obrigatorio and string == '':
                return ''
            if string == '':
                print('ERRO: O campo não pode ficar vazio!')
                continue
            return string
        except(KeyboardInterrupt):
            print('Usuário preferiu não digitar.')
            return '<desconhecido>'


def validar_int(msg, obrigatorio=True):
    while True:
        try:
            entrada = input(msg).strip()
            if not obrigatorio and entrada == '':
                return None
            valor = int(entrada)
            return valor
        except(ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido!')
        except(KeyboardInterrupt):
            print('Usuario preferiu não digitar.')
            return 0
        

def validar_email(msg, obrigatorio=True):
    while True:
        try:
            email = str(input(msg)).strip().lower()
            if not obrigatorio and email == '':
                return ''
            if obrigatorio and email == '':
                print('ERRO: O campo e-mail não pode ficar vazio!')
                continue
            if '@' not in email or '.' not in email:
                print('ERRO: Digite um e-mail válido (exemplo@dominio.com)!')
                continue
            return email
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar.')
            return '<desconhecido>'
    

def validar_celular(msg, obrigatorio=True):
    while True:
        try:
            entrada = str(input(msg)).strip()
            apenas_numeros = "".join(char for char in entrada if char.isdigit())
            if not obrigatorio and apenas_numeros == '':
                return ''
            if obrigatorio and apenas_numeros == '':
                print('ERRO: O campo celular não pode ficar vazio!')
                continue
            if len(apenas_numeros) != 11:
                print('ERRO: O celular deve ter 11 dígitos (DDD + número)!')
                continue
            return apenas_numeros
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar.')
            return '00000000000'
def validar_str(msg, obrigatorio=True):
    while True:
        try:
            string = str(input(msg)).strip()
            if string == '':
                print('ERRO: O campo não pode ficar vazio!')
                continue
            if not obrigatorio and string == '':
                return ''
        except(KeyboardInterrupt):
            print('Usuário preferiu não digitar.')
            return '<desconhecido>'
        return string


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
        else:
            return valor
        

def validar_email(msg, obrigatorio=True):
    while True:
        try:
            email = str(input(msg)).strip().lower()
            if email == '':
                print('ERRO: O campo e-mail não pode ficar vazio!')
                continue
            if '@' not in email or '.' not in email:
                print('ERRO: Digite um e-mail válido (exemplo@dominio.com)!')
                continue
            if not obrigatorio and email == '':
                return ''
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o e-mail.')
            return '<desconhecido>'
        return email
    

def validar_celular(msg, obrigatorio=True):
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
            if not obrigatorio and apenas_numeros == '':
                return ''
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o celular.')
            return '00000000000'
        return apenas_numeros
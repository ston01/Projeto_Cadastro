def validar_str(msg, obrigatorio=True):
    while True:
        try:
            string = str(input(msg)).strip()
            if not obrigatorio and string == '':
                return ''
            if string == '':
                print('\033[31mERRO: O campo não pode ficar vazio!\033[0m')
                continue
            return string
        except(KeyboardInterrupt):
            print('\033[33mUsuário preferiu não digitar.\033[0m')
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
            print('\033[31mERRO: Digite um número inteiro válido!\033[0m')
        except(KeyboardInterrupt):
            print('\033[33mUsuario preferiu não digitar.\033[0m')
            return 0
        

def validar_email(msg, obrigatorio=True):
    while True:
        try:
            email = str(input(msg)).strip().lower()
            if not obrigatorio and email == '':
                return ''
            if obrigatorio and email == '':
                print('\033[31mERRO: O campo e-mail não pode ficar vazio!\033[0m')
                continue
            if '@' not in email or '.' not in email:
                print('\033[31mERRO: Digite um e-mail válido (exemplo@dominio.com)!\033[0m')
                continue
            return email
        except (KeyboardInterrupt):
            print('\033[33mUsuário preferiu não digitar.\033[0m')
            return '<desconhecido>'
    

def validar_celular(msg, obrigatorio=True):
    while True:
        try:
            entrada = str(input(msg)).strip()
            apenas_numeros = "".join(char for char in entrada if char.isdigit())
            if not obrigatorio and apenas_numeros == '':
                return ''
            if obrigatorio and apenas_numeros == '':
                print('\033[31mERRO: O campo celular não pode ficar vazio!\033[0m')
                continue
            if len(apenas_numeros) != 11:
                print('\033[31mERRO: O celular deve ter 11 dígitos (DDD + número)!\033[0m')
                continue
            return apenas_numeros
        except (KeyboardInterrupt):
            print('\033[33mUsuário preferiu não digitar.\033[0m')
            return '00000000000'
        

def enter_continuar():
    try:
        input('\nPressione Enter para continuar...')
    except (KeyboardInterrupt):
        print(' \033[33mUsuário preferiu não digitar.\033[0m ')
        exit()
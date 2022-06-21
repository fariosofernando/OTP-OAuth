# Quando ele for a pedir o OTP, abra o arquivo cache/generated_otp.txt.
# Digite ele para que o usuario logue no sistema.

# import o OTP
from generator import OTP

# Uma funcao simples para a simulacao de login de usuarios em um sistema.
def login():

    user = input(str('USER: '))
    password = input(str('SENHA: '))
    
    # generate otp
    otp = OTP().generate()

    # Digite o OTP localizado no arquivo cache/generated_otp.txt
    confirm = input(str('OTP: '))
   
    # Confirmando se é compativel como o OTP gerado.
    with open('./cache/generated_otp.txt', 'r') as file:
        otp = file.read()

    if confirm == otp: print('Logado com sucesso')
    else: print('Codigo de verificacao invalido')

# Chamando a simulacao de login.
login()
# O pacote random será o responsavel por selecionar elementos aleartorios
# na nossa lista de numeros
import random

class OTP:
    '''...'''
    def __init__(self) -> None:
        
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.txt = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J'] # Ultimo caractere.
        self.otp_code = ''

    def generate(self):

        while True:
            select = random.randrange(0, 10)

            if(len(self.otp_code) <= 3): 
                self.otp_code += '{}'.format(self.nums[select])
            else:
                self.otp_code += '{}'.format(self.txt[select])
                try:
                    with open('./cache/generated_otp.txt', 'w') as file:
                        file.write(self.otp_code); 
                    return True   
                    break
                except:
                    return False
                    break
            


#2528

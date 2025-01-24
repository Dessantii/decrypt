import os
import pyaes
import random

def gerar_conta():
  
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
  
    operador = random.choice(['+', '-'])
 
    pergunta = f"{num1} {operador} {num2}"
    resposta_correta = eval(pergunta)  
    
    return pergunta, resposta_correta

def descriptografar(arquivo_criptografado, chave):
    try:
        if not os.path.isfile(arquivo_criptografado):
            raise FileNotFoundError(f"O arquivo criptografado '{arquivo_criptografado}' não foi encontrado.")
        
        pergunta, resposta_correta = gerar_conta()
        print(f"Para continuar, resolva a seguinte operação matemática: {pergunta}")

        resposta_usuario = int(input("Sua resposta: "))

        if resposta_usuario != resposta_correta:
            print("Resposta incorreta. Descriptografação não permitida.")
            return

        with open(arquivo_criptografado, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(chave)
        decrypt_data = aes.decrypt(file_data)

        arquivo_descriptografado = arquivo_criptografado.replace(".ransomwaretroll", "")
        
        with open(arquivo_descriptografado, "wb") as new_file:
            new_file.write(decrypt_data)

        os.remove(arquivo_criptografado)

        print(f"Arquivo '{arquivo_criptografado}' descriptografado com sucesso para '{arquivo_descriptografado}'!")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

arquivo_criptografado = "projeto.txt.ransomwaretroll"  # Substitua pelo nome do seu arquivo criptografado
chave = b"testeransomwares" 
descriptografar(arquivo_criptografado, chave)

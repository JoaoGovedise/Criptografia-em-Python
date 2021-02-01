from urllib.parse import quote, unquote


def cipher_criptografar():
    msg = input("Digite a mensagem para criptografar: ")
    chave = input("Digite uma senha: ")
    msg = quote(msg)

    criptografar_hex = ""
    chave_itr = 0

    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(chave[chave_itr])
        criptografar_hex += hex(temp)[2:].zfill(2)
        chave_itr += 1
        if chave_itr >= len(chave):
            chave_itr = 0

    print(f"Criptografar text: {criptografar_hex}")
    
    print("------------------------------------------------------------------------------")  
    return main()
    

   
def cipher_descriptografar():
    msg = input("Digite a Mensagem criptografada: ")
    chave = input("Digite a senha da criptografia: ")

    hex_to_uni = ""
    for i in range(0, len(msg), 2):
        hex_to_uni += bytes.fromhex(msg[i:i+2]).decode("utf-8")

    descriptografar_text = ""
    chave_itr = 0

    for i in range(len(hex_to_uni)):
        temp = ord(hex_to_uni[i]) ^ ord(chave[chave_itr])
        descriptografar_text += chr(temp)
        chave_itr += 1
        if chave_itr >= len(chave):
            chave_itr = 0

    descriptografar_text = unquote(descriptografar_text)
    print(f"Descriptografar text: {descriptografar_text}")

    print("------------------------------------------------------------------------------")

    return main()

def main():
    escolha = int(input("1. Criptografar \n2. Descriptografar \n0. Sair do Programa\nEscolha(1,2,0): "))
    if escolha == 1:
        print("    Criptografar    ")
        cipher_criptografar()
    elif escolha == 2:
        print("     Descriptografar   ")
        cipher_descriptografar()
    elif escolha == 0:
        print("  Programa Finalizado   ")
    else:
        print("Escolha Invalida")
if __name__ == "__main__":
    main()


        
      

        
        

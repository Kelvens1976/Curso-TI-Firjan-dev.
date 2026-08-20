def validacao(matricula_usuario,senha_usuario):
 return matricula_usuario == "121976" and senha_usuario == "1234"

def login():
    tentativas = 3
    for tentativa in range(1,tentativas+1):
        matricula_usuario = input("Entre com a matricula: ")
        senha_usuario = input ("Entre com a Senha: ")

        if validacao(matricula_usuario,senha_usuario):
            print("Bem Vindo! Acesso Autorizado!")
            return
        
        tentativas = tentativas - tentativa
    
        if tentativas > 0:
           print("Você ainda tem: ", tentativas)
           return
        
    print("Acesso Bloqueado !!!!")
login()
    
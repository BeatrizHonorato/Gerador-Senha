import string
import secrets

def case1():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 2):
            break
    print(f"A senha gerada é: {password}")
    input("Pressione Enter para fechar o programa.")

def case2():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(12))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 5):
            break
    print(f"A senha gerada é: {password}")
    input("Pressione Enter para fechar o programa.")

def case3():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(18))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 9):
            break
    print(f"A senha gerada é: {password}")
    input("Pressione Enter para fechar o programa.")

def case4():
    print("Saindo...")

user_input = int(input("Escolha uma opção: (1 - Facil, 2 - Medio, 3 - Dificil, 4 - Sair):"))

switch_dic ={
    1: case1,
    2: case2,
    3: case3,
    4: case4
}

if user_input in switch_dic:
    switch_dic[user_input]()
else:
    print("Opção inválida.")

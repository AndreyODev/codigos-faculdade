import random

# Introdução ao jogo
print('''Você, ouviu rumores sobre uma masmorra antiga guardada por um temível dragão. 
Dizem que dentro dela existem riquezas inimagináveis e um artefato lendário que pode trazer paz ao reino.''')

# Definição das estatísticas do personagem do jogador
prota = {
    "nome": "Você",
    "vida": 100,
    "forca": 20,
    "cura": 15
}

# Definição dos goblins
goblins = [{"nome": "Goblin 1", "vida": 30, "forca": 8},
           {"nome": "Goblin 2", "vida": 30, "forca": 8},{"nome": "Goblin 3", "vida": 30, "forca": 8}]

# Definição do guardiao esqueleto
guardiao_esqueleto = {
    "nome": "Guardião Esqueleto",
    "vida": 60,
    "forca": 15
}                            

# Definição do dragao
dragao = {
    "nome": "Dragão",
    "vida": 120,
    "forca": 20
}
# Função para mostrar o estado atual do jogo
def mostrar_estado(estado):
    print(f"{estado['nome']}: Vida = {estado['vida']}")

# Função de ataque
def atacar(atacante, defensor):
    dano = random.randint(0, atacante["forca"])
    defensor["vida"] -= dano
    print(f"{atacante['nome']} atacou {defensor['nome']} causando {dano} de dano.")

# Função de cura
def curar(jogador):
    cura = random.randint(0, jogador["cura"])
    jogador["vida"] += cura
    print(f"{jogador['nome']} se curou e recuperou {cura} de vida.")

# Parte 1: Enfrentando os Goblins
print("Parte 1: Enfrentando os Goblins")
for goblin in goblins:
    while goblin["vida"] > 0 and prota["vida"] > 0:
        mostrar_estado(prota)
        mostrar_estado(goblin)
        print("Escolha uma ação:")
        print("1. Atacar")
        print("2. Curar")
        escolha = input("Digite o número da ação: ")
        if escolha == "1":
            atacar(prota, goblin)
        elif escolha == "2":
            curar(prota)
        else:
            print("Escolha inválida. Tente novamente.")
            continue

        if goblin["vida"] > 0:
            atacar(goblin, prota)
        if prota["vida"] <= 0:
            print("Você foi derrotado pelos goblins. Fim do jogo.")
 
print("Você derrotou todos os goblins e pode prosseguir para a próxima etapa.")

print("Parte 2: Enfrentando o Guardião Esqueleto")
while guardiao_esqueleto["vida"] > 0 and prota["vida"] > 0:
    mostrar_estado(prota)
    mostrar_estado(guardiao_esqueleto)
    print("Escolha uma ação:")
    print("1. Atacar")
    print("2. Curar")
    escolha = input("Digite o número da ação: ")
    if escolha == "1":
        atacar(prota, guardiao_esqueleto)
    elif escolha == "2":
        curar(prota)
    else:
        print("Escolha inválida. Tente novamente.")
        continue

    if guardiao_esqueleto["vida"] > 0:
        atacar(guardiao_esqueleto, prota)
    else:
        print("Você derrotou o Guardião Esqueleto e pode prosseguir para a próxima etapa.")
    if prota["vida"] <= 0:
        print("Você foi derrotado pelo Guardião Esqueleto. Fim do jogo.")

print("Parte 3: Enfrentando o Dragão")
while dragao["vida"] > 0 and prota["vida"] > 0: 
    mostrar_estado(prota)
    mostrar_estado(dragao)
    print("Escolha uma ação:")
    print("1. Atacar")
    print("2. Curar")
    escolha = input("Digite o número da ação: ")
    if escolha == "1":
        atacar(prota, dragao)
    elif escolha == "2":
        curar(prota)
    else:
        print("Escolha inválida. Tente novamente.")
        continue

    if dragao["vida"] > 0:
        atacar(dragao, prota)
    else:
        print('''Você derrotou o Dragão e obteve o artefato lendário que trará paz ao reino. 
                Parabéns, você venceu o jogo!''')
    
    if prota["vida"] <= 0:
        print("Você foi derrotado pelo Dragão. Fim de jogo.")



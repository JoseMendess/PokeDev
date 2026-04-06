import csv
import requests
import matplotlib.pyplot as plt
import numpy as np

def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)
    #verificação de erro
    if resposta.status_code != 200:
        print(f"Erro ao buscar")
        return None
    dados = resposta.json()
    #organização dos dados
    stats = {}
    for stat in dados["stats"]:
        nome_stat = stat["stat"]["name"]
        valor = stat["base_stat"]
        stats[nome_stat] = valor
    pokemon = {
        "nome": dados["name"],
        "vida": stats["hp"],
        "ataque": stats["attack"],
        "defesa": stats["defense"],
        "velocidade": stats["speed"]
    }
    return pokemon

def simular_batalha(p1, p2):
    vida1 = p1["vida"]
    vida2 = p2["vida"]

    print(f"\n Batalha: {p1['nome'].capitalize()} vs {p2['nome'].capitalize()}\n")

    turno = 1

    while vida1 > 0 and vida2 > 0:
        print(f"Turno {turno}")

        dano1 = max(1, p1["ataque"] - p2["defesa"])
        dano2 = max(1, p2["ataque"] - p1["defesa"])

        vida2 -= dano1
        print(f"{p1['nome']} causou {dano1} de dano!")

        if vida2 <= 0:
            print(f"\n {p1['nome'].capitalize()} venceu!")
            return p1["nome"]

        vida1 -= dano2
        print(f"{p2['nome']} causou {dano2} de dano!")

        if vida1 <= 0:
            print(f"\n {p2['nome'].capitalize()} venceu!")
            return p2["nome"]

        print(f"Vida {p1['nome']}: {vida1} | Vida {p2['nome']}: {vida2}\n")

        turno += 1

def salvar_resultado(p1, p2, vencedor):
    with open("historico_batalhas.csv", mode="a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([p1["nome"], p2["nome"], vencedor])

def grafico_radar(p1, p2):
    categorias = ["vida", "ataque", "defesa", "velocidade"]

    valores1 = [p1[c] for c in categorias]
    valores2 = [p2[c] for c in categorias]

    valores1 += valores1[:1]
    valores2 += valores2[:1]

    angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
    angulos += angulos[:1]

    plt.figure()
    ax = plt.subplot(111, polar=True)

    ax.plot(angulos, valores1, label=p1["nome"])
    ax.fill(angulos, valores1, alpha=0.1)

    ax.plot(angulos, valores2, label=p2["nome"])
    ax.fill(angulos, valores2, alpha=0.1)

    ax.set_thetagrids(np.degrees(angulos[:-1]), categorias)
    plt.legend()
    plt.title("Comparação de Status")
    plt.show()

def main():
    nome1 = input("Digite o nome do primeiro Pokémon: ")
    nome2 = input("Digite o nome do segundo Pokémon: ")

    p1 = buscar_pokemon(nome1)
    p2 = buscar_pokemon(nome2)

    if not p1 or not p2:
        print("Erro ao buscar Pokémon.")
        return

    vencedor = simular_batalha(p1, p2)

    salvar_resultado(p1, p2, vencedor)

    grafico_radar(p1, p2)
    main()
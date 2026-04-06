import requests
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


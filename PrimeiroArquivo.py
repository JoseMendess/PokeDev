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

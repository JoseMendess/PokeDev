import requests
def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)
    dados = resposta.json()

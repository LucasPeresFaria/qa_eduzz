import requests
import json

class Listagem_pokemon():
    def __init__(self, nome):
        self._nome = nome

    def requisicao_api(self):
            request = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self._nome}')
            if request.status_code == 200:
                return request.json()
            else:
                return request.status_code

    def imprime_validacao_nome(self):
        dados_pokemon = self.requisicao_api()

        if dados_pokemon['name'] == 'ditto':
            print('O Pokemon se chama DITTO, esta correto!')
        else:
            print('Não se chama DITTO, é ' + str(dados_pokemon['name']))
        
    def imprime_validacao_id(self):
        dados_pokemon = self.requisicao_api()

        if dados_pokemon['id'] == 132:
            print("O número do Pokemon é 132, está correto!")
        else:
            print("O número do Pokemon não é 132, é " + str(dados_pokemon['id']))
    
    def imprime_validacao_tipo(self):
        dados_pokemon = self.requisicao_api()

        if dados_pokemon['types'][0]['type']['name'] == 'normal':
            print('É um Pokemon do tipo ' + str(dados_pokemon['types'][0]['type']['name']) + "\n")
        else:
            print('Não é um Pokemon do tipo Normal, é do tipo '+ str(dados_pokemon['types'][0]['type']['name']) + "\n")
        
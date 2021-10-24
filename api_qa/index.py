from func import Listagem_pokemon

arquivo = 'C:/Users/Lucas/Desktop/Prova/api_qa/entrada.txt'

with open(arquivo) as file_object:
    for line in file_object:
        if(line==''):
            break
        else:
            buscar_pokemon = Listagem_pokemon(line.rstrip())
            buscar_pokemon.imprime_validacao_nome()
            buscar_pokemon.imprime_validacao_id()
            buscar_pokemon.imprime_validacao_tipo()

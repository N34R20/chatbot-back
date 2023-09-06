import os
import json
from functions_pipe import search_loop, dump_json

DATA_ROUTE = "/Users/franciscoolmos/Github/chatbot-back/data"
print("confirmo que sea el directorio de la data\n", DATA_ROUTE)

# Obtener una lista de todos los elementos en el directorio actual
all_elements = os.listdir(DATA_ROUTE)

# Filtrar solo los directorios
directories = [element for element in all_elements if os.path.isdir(os.path.join(DATA_ROUTE, "/", element))]

print("Directorios en el directorio actual:", directories)


# creo el json 
file_dictionary = search_loop(DATA_ROUTE)
file_name = 'poems.json'

dump_json(file_name, file_dictionary)

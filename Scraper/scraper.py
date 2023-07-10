import requests
from bs4 import BeautifulSoup

# Realizar la solicitud HTTP GET a la página web
url = input("inserte pagina web: \n")
response = requests.get(url)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Crear el objeto BeautifulSoup con el contenido HTML de la respuesta
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
else:
    print('Error al realizar la solicitud HTTP:', response.status_code)

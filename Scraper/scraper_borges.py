import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


# Realizar la solicitud HTTP GET a la página web
url = 'https://www.poemas-del-alma.com/jorge-luis-borges.htm'
response = requests.get(url)

poemas_url = []

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Crear el objeto BeautifulSoup con el contenido HTML de la respuesta
    soup = BeautifulSoup(response.content, 'html.parser')
    # Encontrar el tag <div> con la clase "container-list-poems-2"
    div = soup.find('div', class_='container-list-poems-2')
    # Verificar si se encontró el tag <div> y si contiene una lista
    if div and div.ul:
        # Encontrar todos los elementos <li> dentro del tag <div>
        lista = div.ul.find_all('li')
        # Imprimir los elementos de la lista
        for elemento in lista:
#            poemas.append(elemento.text)
            a_tag = elemento.find('a')
            href = a_tag.get('href')
            poemas_url.append(href)
        
    else:
        print('No se encontró la lista dentro del tag <div> con la clase "container-list-poems-2"')
else:
    print('Error al realizar la solicitud HTTP:', response.status_code)


for poema in poemas_url:
    response = requests.get('https://www.poemas-del-alma.com/' + poema)
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', class_='poem-entry')
    print(div.find_all('p'))
#    print(soup)
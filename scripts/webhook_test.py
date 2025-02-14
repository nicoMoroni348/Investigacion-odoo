import requests
import json

# Primero se obtiene la url del webhook y se define el cuerpo del mensaje
webhook_url = 'http://127.0.0.1:5000/webhook'
data_nico = {   'nombre': 'Nico',
                'apellido': 'Moroni' }

# Usamos el objeto request con sus respectivos parámetros:
# El objeto request literalmente hace una petición HTML, 
# en este caso con el método post (xq queremos mandar información)
# Los parámetros del post son:
# - url: usamos la variable que almacenamos
# - data: información que queremos mandar. 
#   Conviene formatearla en JSON usando "json.dumps()"
# - http headers: acá definimos la cabecera del mensaje. 
# Especificamos, por ejemplo, el formato de mensaje JSON

r = requests.post(
        webhook_url, 
        data=json.dumps(data_nico), 
        headers={'Content-Type': 'application/json'})
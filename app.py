#Importar las bibliotecas necesarias de Flask
from flask import Flask, render_template, request
#Importar la biblioteca requests para realizar solicitudes HTTP
import requests
#Crear una instancia de la aplicación Flask
app = Flask(__name__)
#Definir la URL base de la PokeAPI
url_api = 'https://pokeapi.co/api/v2/pokemon/'


#Ruta para la página principal, muestra index.html
@app.route('/')
def index():
    return render_template('index.html')

#Ruta para una página de prueba, muestra prueba.html
@app.route("/prueba")
def prueba():
    return render_template('prueba.html')

#Ruta para buscar y mostrar información sobre un Pokémon
@app.route('/pokemon', methods=['GET', 'POST'])
def Pokemon():
    if request.method == 'POST':
        #Obtener el nombre del Pokémon enviado desde el formulario
        pokemon_name = request.form['pokemon_name']
        #Construir la URL completa para obtener datos del Pokémon
        pokemon_data_url = url_api + pokemon_name
         #Obtener datos del Pokémon llamando a la función get_pokemon_data
        data = get_pokemon_data(pokemon_data_url)
        #Renderizar la plantilla pokemon.html con los datos del Pokémon
        return render_template('pokemon.html', pokemon_data=data)
     #Si la solicitud es GET, simplemente mostrar la plantilla pokemon.html
    return render_template('pokemon.html')

#Función para obtener datos de un Pokémon desde la PokeAPI
def get_pokemon_data(url_pokemon=''):
    #Crear un diccionario para almacenar los datos del Pokémon
    pokemon_data = {
        "name": '',
        "habilities": '',
        "types": '',
        "image_url": ''
    }

    #Realizar una solicitud GET a la PokeAPI con la URL proporcionada
    response = requests.get(url_pokemon)
    #Convertir la respuesta a formato JSON
    data = response.json()

    #Extraer información relevante del JSON devuelto por la PokeAPI
    pokemon_data['name'] = data['name']
    pokemon_data['habilities'] = len(data['abilities'])
    pokemon_data['types'] = data['types']
    pokemon_data['image_url'] = data['sprites']['front_default']
    
    #Devolver los datos del Pokémon
    return pokemon_data

 #Ejecutar la aplicación Flask en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)

#Proximamente agregar la lista completa de todos los pokemon existentes!
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url_api = 'https://pokeapi.co/api/v2/pokemon/'


#ruta para probar todas las etiquetas
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/prueba")
def prueba():
    return render_template('prueba.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def Pokemon():
    if request.method == 'POST':
        pokemon_name = request.form['pokemon_name']
        pokemon_data_url = url_api + pokemon_name
        data = get_pokemon_data(pokemon_data_url)
        return render_template('pokemon.html', pokemon_data=data)
    return render_template('pokemon.html')


def get_pokemon_data(url_pokemon=''):
    pokemon_data = {
        "name": '',
        "habilities": '',
        "types": '',
        "image_url": ''
    }

    response = requests.get(url_pokemon)
    data = response.json()

    pokemon_data['name'] = data['name']
    pokemon_data['habilities'] = len(data['abilities'])
    pokemon_data['types'] = data['types']
    pokemon_data['image_url'] = data['sprites']['front_default']
    
    return pokemon_data


if __name__ == '__main__':
    app.run(debug=True)
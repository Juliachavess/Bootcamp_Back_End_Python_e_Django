from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

def fetch_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    return json.loads(data)

def fetch_character_by_id(character_id):
    try:
        url = f"https://rickandmortyapi.com/api/character/{character_id}"
        response = urllib.request.urlopen(url)
        data = response.read()
        return json.loads(data)
    except Exception as e:
        print(f"Error fetching character data: {e}")
        return None


def fetch_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    data = response.read()
    return json.loads(data)

@app.route("/")
def get_list_characters_page():
    data = fetch_characters()
    return render_template("character.html", characters=data["results"])

@app.route('/character/<int:id>')
def character_profile(id):
    character = fetch_character_by_id(id)
    if character:
        return render_template('character_profile.html', character=character)
    else:
        return "Personagem não encontrado", 404



@app.route("/lista")
def get_list_elements():
    data = fetch_characters()
    characters = [{"name": character["name"], "status": character["status"]} for character in data["results"]]
    return {"characters": characters}

@app.route("/locations")
def get_locations():
    data = fetch_locations()
    locations = [{"id": location["id"], "name": location["name"], "type": location["type"], "dimension": location["dimension"]} for location in data["results"]]
    return render_template("locations.html", locations=locations)

@app.route('/location/<id>')
def location_profile(id):
    if not id.isdigit():
        return "ID inválido", 400  # Verifica se o ID é um número
    
    id = int(id)  # Converte o ID para inteiro
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    location = json.loads(data)
    
    # Obtenha URLs dos residentes
    resident_urls = location.get('residents', [])
    
    # Busque os detalhes dos residentes
    residents = []
    for url in resident_urls:
        try:
            res_response = urllib.request.urlopen(url)
            res_data = res_response.read()
            resident = json.loads(res_data)
            residents.append(resident)
        except Exception as e:
            print(f"Error loading resident data: {e}")
            # Pode adicionar tratamento adicional de erros aqui

    return render_template('location_profile.html', location=location, residents=residents)


@app.route('/episodes')
def list_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    episodes = json.loads(data)['results']
    return render_template('episodes.html', episodes=episodes)

@app.route('/episodes/<int:episode_id>')
def episode_profile(episode_id):
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    episode = json.loads(data)
    return render_template('episode_profile.html', episode=episode)

if __name__ == "__main__":
    app.run(debug=True)

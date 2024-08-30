from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

def fetch_characters():
    url = "https://rickandmortyapi.com/api/character"
    response = urllib.request.urlopen(url)
    data = response.read()
    return json.loads(data)

def fetch_character_by_id(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    return json.loads(data)

@app.route("/")
def get_list_characters_page():
    data = fetch_characters()  # Use a função auxiliar para buscar os dados
    return render_template("character.html", characters=data["results"])  # Passe os dados para o template

@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return render_template("profile.html", profile=data)


@app.route("/lista")
def get_list_elements():
    data = fetch_characters()  # Use a função auxiliar para buscar os dados
    characters = []

    for character in data["results"]:
        char_info = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(char_info)

    return {"characters": characters}

if __name__ == "__main__":
    app.run(debug=True)

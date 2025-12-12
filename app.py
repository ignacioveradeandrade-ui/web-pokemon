from flask import Flask , render_template

app = Flask(__name__)

datos = {
    1 : ["Pikachu" , "Electrico" , "Raichu"],
    2 : ["Charmander" , "Fuego" , "Charizard"],
    3 : ["Burbasaur" , "Agua" , "Blastoide"]
}

@app.route("/")
def home():
    return render_template("index.html" , pokemons = datos)

@app.route("/pokemons-legendarios")
def legendarios():
    return render_template("legendarios.html")


if __name__ == "__main__":
    app.run(debug=True)

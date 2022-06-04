from flask import Flask, render_template, request, redirect, session
import requests

# API DEL CLIMA
api_key = "2a4ae7462bb2c3d9679bd93deb6664c6"  # Enter the API key you got from the OpenWeatherMap website
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# calcular clima ciudad quito
city_name = "Quito"
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
response = requests.get(complete_url)
x = response.json()

intro = "El clima de " + city_name + " es: "
if x["cod"] != "404":
    y = x["main"]

    current_temperature = round(x["main"]["temp"] - 273, 15)
    z = x["weather"]

# calcular clima ciudad cartagena
city_name1 = "Cartagena"
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name1
response = requests.get(complete_url)
xx = response.json()

if xx["cod"] != "404":
    y = xx["main"]

    current_temperature1 = round(xx["main"]["temp"] - 273, 15)
    z = xx["weather"]

app = Flask(__name__)
app.secret_key = 'clavesecreta'

user = {"username": "abc", "password": "xyz"}


# =============================================RUTAS================================================================
# route quito

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            session['user'] = username
            return redirect('/clima')

        return "<h1>Usuario o contraseña incorrectas</h1>"
    return render_template("login.html")


@app.route('/clima')
def index():
    return render_template("index.html")


# route quito
@app.route('/quito')
def home():
    return render_template("quito.html", climaQuito=round(current_temperature))


# route cartagena
@app.route('/cartagena')
def home1():
    return render_template("cartagena.html", Cartagena=round(current_temperature1))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


# listen
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    api_key = '9108dea7ba0db115b547dc98d6e84f25'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/', methods=['GET', 'POST'])
def index():
    city = None
    temperature = None
    description = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']

    return render_template('index.html', city=city, temperature=temperature, description=description)

if __name__ == '__main__':
    app.run(debug=True)
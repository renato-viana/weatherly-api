from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather_data():
    # URL do seu cluster OpenSearch
    url = "http://localhost:9200/weather-data/_doc/1"

    # Fazendo a requisição GET para o OpenSearch
    response = requests.get(url)

    # Verificando se a requisição foi bem sucedida
    if response.status_code == 200:
        # Retornando os dados do documento
        return response.json()
    else:
        return {"error": "Não foi possível obter os dados."}

@app.route('/weather', methods=['POST'])
def post_weather_data():
    # Dados a serem inseridos
    data = {
        "timestamp": "2021-11-01T14:05:00Z",
        "station-id": 142,
        "temperature": 14.7,
        "wind-speed": 5.2,
        "wind-direction": "SSE",
        "pressure": 1013,
        "rainfall-rate": 0
    }

    # URL do seu cluster OpenSearch
    url = "http://localhost:9200/weather-data/_doc"

    # Fazendo a requisição POST para o OpenSearch
    response = requests.post(url, data=json.dumps(data))

    # Verificando se a requisição foi bem sucedida
    if response.status_code == 201:
        # Retornando a confirmação de sucesso
        return {"success": "Dados inseridos com sucesso."}
    else:
        return {"error": "Não foi possível inserir os dados."}

if __name__ == '__main__':
    app.run(debug=True)

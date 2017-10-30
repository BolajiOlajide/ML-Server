from flask import Flask, jsonify, request
import dotenv

from helper import emulate_ml_model

app = Flask(__name__)

dotenv.load()

@app.route('/')
def index():
    return 'API is working!'


@app.route('/ml', methods=['POST'])
def ml():
    json_input = request.json
    output_data = emulate_ml_model(json_input)
    return jsonify({ 'data': output_data })

print(dotenv.get('PORT'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=dotenv.get('PORT', 8080))

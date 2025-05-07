from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Servicio 1 (node1)
@app.route('/node1')
def node1():
    try:
        response = requests.get('http://127.0.0.1:5000/data')  # Petición al primer servicio
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Error al conectar con node1: {str(e)}"}), 500

# Servicio 2 (node2)
@app.route('/node2')
def node2():
    try:
        response = requests.get('http://127.0.0.1:8000/data')  # Petición al segundo servicio
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": f"Error al conectar con node2: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=4000)  # API Gateway en puerto 4000

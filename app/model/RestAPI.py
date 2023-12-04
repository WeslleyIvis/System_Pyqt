from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def get_status():
    return ({'status': 5})

@app.route('/login', methods=['POST'])
def request_login():
    if request.is_json:
        dados = request.json

        print(f"Dados: ", dados)

        return jsonify({'message': 'data sent'}), 200
    else:
        return jsonify({'message': 'request is not a JSON'}), 400
        


if __name__ == '__main__':
    app.run(debug=True)
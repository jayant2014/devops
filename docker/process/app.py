from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    msg = "Hello World!"
    response = jsonify(msg)
    response.status_code = 200
    return response

@app.route('/v1/<host>', methods=['GET', ])
def health_check(host):
    resp_data = dict()
    resp_data["ssd"] = "128GB"
    resp_data["cpu"] = "4 Cores"
    resp_data["ram"] = "8GB"
    response = jsonify(resp_data)
    response.status_code = 400
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')

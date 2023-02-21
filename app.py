from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello_world():
    return {"message": "Hello World!!"}, 200

@app.get("/todo")
def todo():
    return {"message": "Todo app Successfully running!!", "data": [1,2]}, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
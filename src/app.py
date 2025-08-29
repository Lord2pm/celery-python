from flask import Flask, jsonify

from tasks import hello

app = Flask(__name__)


@app.get("/")
def root():
    hello.delay("Luís")
    return jsonify({"msg": "Olá, mundo"})

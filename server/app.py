from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route("/")
def index():
    # возвращаем текстовый файл
    return send_file("data.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

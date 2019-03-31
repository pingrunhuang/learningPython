from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/<int:seed>")
def index(seed):
    random.seed(seed)
    time.sleep(2)
    return str(random.randint(0, 10))

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
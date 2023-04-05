from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print('Received request:', request.method, request.url)
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(port=5000)
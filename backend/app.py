from flask import Flask
import requests

app = Flask(__name__)

client_id = "8579eecb870c7b951747179173cfb634"

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/api')
def api_root():
    


if __name__ == '__main__':
    app.run(debug=True)

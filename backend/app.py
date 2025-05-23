# running flask template
from flask import Flask, request, josnify

app = Flask(__name__)

@app.route('/calculate_equity')

def calculate_equity():
    data = request.json

if __name__ == '__main__':
    app.run()
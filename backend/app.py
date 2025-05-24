# running flask template
from flask import Flask, request, josnify
from equity import calculate_equity

app = Flask(__name__)

@app.route('/calculate_equity', methods=['POST'])

def calculate_equity():
    data = request.json

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify
import random
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

fashion_quotes = [
    "Fashion is the armor to survive the reality of everyday life. – Bill Cunningham",
    "Style is a way to say who you are without having to speak. – Rachel Zoe",
    "Dress like you're already famous.",
    "Fashion fades, only style remains the same. – Coco Chanel",
    "Don't be into trends. Don't make fashion own you. – Gianni Versace",
    "Elegance is not standing out, but being remembered. – Giorgio Armani",
    "Life is too short to wear boring clothes.",
    "People will stare. Make it worth their while. – Harry Winston"
]

@app.route('/fashion-quote', methods=['GET'])
def get_quote():
    quote = random.choice(fashion_quotes)
    return jsonify({'quote': quote})

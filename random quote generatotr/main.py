from flask import Flask, render_template, jsonify
import requests
import json
app = Flask(__name__)

def random_quote():
    url = "https://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        quote_data = response.json()
        quote_text = quote_data["quoteText"]
        quote_author = quote_data["quoteAuthor"]
        return {"quote_text": quote_text, "quote_author": quote_author}
    else:
        return {"quote_text": "Failed to fetch quote", "quote_author": None}

@app.route('/')
def index():
    quote = random_quote()
    return render_template('index.html', quote=quote)

@app.route('/new_quote')
def new_quote():
    quote = random_quote()
    return jsonify(quote)

if __name__ == '__main__':
    app.run(debug=False, host= '0.0.0.0')

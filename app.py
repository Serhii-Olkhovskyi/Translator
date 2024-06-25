from flask import Flask, request, render_template
import requests

app = Flask(__name__)

DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"
DEEPL_API_KEY = "241b582b-af6f-4cb1-9213-2bdc1759c5cc:fx"

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text = request.form['text']
        dest_language = request.form['dest_language']
        params = {
            'auth_key': DEEPL_API_KEY,
            'text': text,
            'target_lang': dest_language.upper()
        }
        response = requests.post(DEEPL_API_URL, data=params)
        if response.status_code == 200:
            translated_text = response.json()['translations'][0]['text']
        else:
            translated_text = "Error: Could not translate text"
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)

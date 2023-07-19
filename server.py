from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchTranslate = translator.english_to_french(textToTranslate)
    return frenchTranslate

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishTranslate = translator.frech_to_english(textToTranslate)
    return englishTranslate 

@app.route("/")
def renderIndexPage():
    return render_template('templates/index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
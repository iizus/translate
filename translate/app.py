from chalice import Chalice
app = Chalice(app_name='translate')

import aws
from urllib import parse

@app.route('/{text}', methods=['GET'])
def translate(text):
    decoded_text = parse.unquote(text)
    translated_text = aws.translate(decoded_text)
    return translated_text
from chalice import Chalice
app = Chalice(app_name='translate')

from chalicelib import aws
from urllib import parse

@app.route(
    '/',
    methods = ['PUT'],
    api_key_required = True,
)
def translate():
    request = app.current_request
    body = request.raw_body
    text = body.decode()
    translated_text = aws.translate(text)
    print(translated_text)
    return translated_text
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
    # text = request.json_body
    text = request.raw_body
    # dic = request.to_dict()
    # text = str(text)
    # text = parse.unquote(text)
    # print(dic)
    print(text.decode())
    return text
    # return text
    # text = str(text)
    # text = parse.quote(text)
    # decoded_text = parse.unquote(text)
    # translated_text = aws.translate(text)
    # translated_text = str(translated_text)
    # translated_text = parse.unquote(translated_text)
    # translated_text = str(translated_text)
    # return translated_text
    # translated_text = str(translated_text)
    # return str(type(translated_text))
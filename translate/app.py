from chalice import Chalice
app = Chalice(app_name='translate')

from chalicelib import aws


def get_text():
    request = app.current_request
    body = request.raw_body
    text = body.decode()
    return text


@app.route(
    '/',
    methods = ['PUT'],
    api_key_required = True,
)
def translate():
    text = get_text()
    translated_text = aws.translate(text)
    print(translated_text)
    return translated_text
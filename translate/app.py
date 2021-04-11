from chalice import Chalice
app = Chalice(app_name='translate')

region = 'ap-northeast-1'

from boto3 import client
translate = client(
    service_name = 'translate',
    region_name = region,
    use_ssl = True,
)

def translate_to_japanese(text):
    response = translate.translate_text(
        Text = text,
        SourceLanguageCode = 'auto',
        TargetLanguageCode = 'ja',
    )
    return response


@app.route('/')
def index():
    response = translate_to_japanese('hello')
    return response
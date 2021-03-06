REGION = 'ap-northeast-1'

ENGLISH = 'en'
JAPANESE = 'ja'

from boto3 import client
translate_client = client(
    service_name = 'translate',
    region_name = REGION,
    use_ssl = True,
)

def translate_to(language, text):
    response = translate_client.translate_text(
        Text = text,
        SourceLanguageCode = 'auto',
        TargetLanguageCode = language,
    )
    translated_text = response.get('TranslatedText')
    source_language = response.get('SourceLanguageCode')
    return translated_text, source_language


def translate_to_japanese(text):
    translated_text, source_language = translate_to(JAPANESE, text)
    return translated_text, source_language


def translate_to_english(text):
    translated_text, source_language = translate_to(ENGLISH, text)
    return translated_text, source_language


def translate(text):
    translated_text, source_language = translate_to_japanese(text)
    if source_language != ENGLISH:
        translated_text, _ = translate_to_english(text)
    return translated_text
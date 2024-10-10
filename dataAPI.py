from translate import Translator


def translate_text(text, src='uz', dest='en'):
    translator = Translator(from_lang=src, to_lang=dest)
    translated = translator.translate(text)
    return translated

def translate_texta(text, src='en', dest='uz'):
    translator = Translator(from_lang=src, to_lang=dest)
    translated = translator.translate(text)
    return translated



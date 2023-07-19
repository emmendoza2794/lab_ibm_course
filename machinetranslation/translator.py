"""Module for language translation """
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """Function to translate from English to French"""
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text



def frech_to_english(french_text):
    """Function to translate from French to English"""
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    print(english_text)
    return english_text

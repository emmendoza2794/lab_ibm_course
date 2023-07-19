import unittest
from machinetranslation.translator import frech_to_english, english_to_french


class TranslationTests(unittest.TestCase):

    def test_frenchToEnglish(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        english_text = frech_to_english(french_text)
        self.assertEqual(english_text, expected_english_text)

    def test_frenchToEnglish_notEqual(self):
        french_text = "Bonjour"
        unexpected_english_text = "Hola"
        english_text = frech_to_english(french_text)
        self.assertNotEqual(english_text, unexpected_english_text)

    def test_englishToFrench(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, expected_french_text)

    def test_englishToFrench_notEqual(self):
        english_text = "Hello"
        unexpected_french_text = "Hola"
        french_text = english_to_french(english_text)
        self.assertNotEqual(french_text, unexpected_french_text)

if __name__ == '__main__':
    unittest.main()

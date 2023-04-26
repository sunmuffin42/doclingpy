from Lexicon import Lexicon
import unittest

class TestLexicon(unittest.TestCase):
    def test_construct_with_words(self):
        words = [
            {"form": "zorro", "gloss": "fox"},
            {"form": "ardilla", "gloss": "squirrel"},
            {"form": "erizo", "gloss": "hedgehog"}
        ]
        lexicon = Lexicon(words=words)
        self.assertEqual(len(lexicon.words), 3)

    def test_construct_with_metadata(self):
        metadata = {"title": "Sample"}
        lexicon = Lexicon(metadata=metadata)
        self.assertEqual(lexicon.metadata["title"], "Sample")

    def test_construct_with_words_and_metadata(self):
        data = {
            "metadata": {"title": "Three Spanish words"},
            "words": [
                {"form": "zorro", "gloss": "fox"},
                {"form": "ardilla", "gloss": "squirrel"},
                {"form": "erizo", "gloss": "hedgehog"}
            ]
        }
        lexicon = Lexicon(**data)
        self.assertEqual(len(lexicon.words), 3)
        self.assertEqual(lexicon.metadata["title"], "Three Spanish words")

    def test_default_sort_by_form(self):
        words = [
            {"form": "zorro", "gloss": "fox"},
            {"form": "ardilla", "gloss": "squirrel"},
            {"form": "erizo", "gloss": "hedgehog"}
        ]
        lexicon = Lexicon(words=words)
        lexicon.sort()
        self.assertEqual(lexicon.words.index({"form": "ardilla", "gloss": "squirrel"}), 0)
        self.assertEqual(lexicon.words.index({"form": "zorro", "gloss": "fox"}), 2)

    def test_has_zorro_fox(self):
        words = [
            {"form": "zorro", "gloss": "fox"},
            {"form": "ardilla", "gloss": "squirrel"},
            {"form": "erizo", "gloss": "hedgehog"}
        ]
        lexicon = Lexicon(words=words)
        self.assertEqual(lexicon.hasWord({"form": "zorro", "gloss": "fox"}), True)

    def test_add_murcielago_bat(self):
        words = [
            {"form": "zorro", "gloss": "fox"},
            {"form": "ardilla", "gloss": "squirrel"},
            {"form": "erizo", "gloss": "hedgehog"}
        ]
        lexicon = Lexicon(words=words)
        bat = {"form": "murcielago", "gloss": "bat"}
        lexicon.addWord(bat)
        self.assertEqual(lexicon.hasWord(bat), True)

    def test_cant_add_zorro_fox_again(self):
        words = [
            {"form": "zorro", "gloss": "fox"},
            {"form": "ardilla", "gloss": "squirrel"},
            {"form": "erizo", "gloss": "hedgehog"}
        ]
        lexicon = Lexicon(words=words)
        fox = {"form": "zorro", "gloss": "fox"}
        beforeLength = len(lexicon.words)
        lexicon.addWord(fox)
        afterLength = len(lexicon.words)
        self.assertEqual(beforeLength, afterLength)

if __name__ == '__main__':
    unittest.main()

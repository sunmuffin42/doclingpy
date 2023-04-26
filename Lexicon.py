class Lexicon:
    def __init__(self, data):
        self.words = data.get('words', [])
        self.metadata = data.get('metadata', {})

    def sort(self):
        self.words.sort(key=lambda word: word['form'])

    def hasWord(self, word):
        return any(w for w in self.words if w['form'] == word['form'] and w['gloss'] == word['gloss'])

    def addWord(self, word):
        if not self.hasWord(word):
            self.words.append(word)

from abc import ABC, abstractmethod
from collections import Counter

class EmptyFileError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class TextAnalyzer():
    slownik = {}
    def __init__(self, filepath):
        self.filepath=filepath
        self.text = self.load_file(filepath)
        self.make_dict()
    def load_file(self, filepath):
        self.filepath= filepath
        try:
            file = open(filepath)
            try:
                self.content = file.read()
                if self.content == False:
                    raise EmptyFileError("Plik jest pusty")
                return self.content
            finally:
                file.close()
        except:
            raise FileNotFoundError("Taki plik nie istnieje")
    def make_dict(self):
        self.content = self.content.lower()
        text = [word for word in self.content.split() if word.isalpha()]
        counter = Counter(text)
        self.slownik = dict(counter)

    def get_word_count(self, word = str):
        try:
            return self.slownik[word]
        except:
            raise KeyError("Nie ma takiego słowa w tekście")
        finally:
            pass

tekst = TextAnalyzer("/dmj/2025/zm488554/p1r/cwiczenia9/plik.txt")
print(tekst.get_word_count("lol"))






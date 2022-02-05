class Line:
    def __init__(self, text: str, chords: str = ""):
        self.text = str(text).replace(u'\xa0', '').strip()
        self.chords = str(chords).strip()

class Verse:
    def __init__(self, lines):
        self.lines = lines

    def __len__(self):
        return len(self.lines)

class Song:
    def __init__(self, name: str, verses: list, author: str = "", extra_info: dict = None ):
        self.name = name.strip()
        self.author = author.strip()
        self.verses = verses
        self.extra_info = extra_info 
    
    def pd2song(lines):
        pass
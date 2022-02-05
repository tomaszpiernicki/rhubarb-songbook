from tracemalloc import start
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5

import sys
sys.path.insert(0, "..")

from xlsx_utils import load_songs_from_xlsx

def print_song_to_pdf():
    print("Warning, this is a test")
    my_canvas = canvas.Canvas("hello.pdf", pagesize=A5)
    my_canvas.drawString(0, 0, "hello żółć!")
    my_canvas.save()

def song_bbox_size():
    pass

if __name__ == "__main__":
    xlsx_path = "E:/rabarbar/rhubarb-songbook/songs_macro.xlsx"
    songs = load_songs_from_xlsx(xlsx_path)

    print(songs[0].name)
    print(songs[0].author)
    print(len(songs[0].verses[0]))

    print(songs[1].name)
    print(songs[1].author)
    print(len(songs[1].verses[0]))

    # print_song_to_pdf()
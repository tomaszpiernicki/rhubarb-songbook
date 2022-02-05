import pandas as pd
from songs import Line, Song, Verse

def raw_to_songs(raw_songs):
    songs = []
    for raw_song in raw_songs:
        header = raw_song.iloc[0][0]
        
        author = ""
        try:
            author, songname = header.split("-")
        except:
            songname = header
        
        verses = []
        lines = []
        for idx, line in raw_song.iloc[1:].iterrows():
            if str(line[0]) != "nan":
                lines.append( Line(*tuple(line)))
            else:
                verses.append(Verse(lines))
                lines = []

        songs.append(Song(songname, verses, author))

    return songs     

def parse_xlsx(xlsx_path):
    df = pd.read_excel(xlsx_path, header=None)
    null_idxs = df[df[df.columns[0]].isnull()].index.tolist()
    null_sep_len = 2
    end_of_song_idxs = [ null_idxs[x] for x in range(len(null_idxs)-null_sep_len+1) 
                             if null_idxs[x] + 1 == null_idxs[x+1] ]

    start_idx = 0
    raw_songs = []
    for end_idx in end_of_song_idxs:
        raw_songs.append(df.iloc[start_idx:end_idx])
        start_idx = end_idx + 2
   
    return raw_songs

def load_songs_from_xlsx(xlsx_path):
    raw_songs = parse_xlsx(xlsx_path)
    songs = raw_to_songs(raw_songs)
    return songs

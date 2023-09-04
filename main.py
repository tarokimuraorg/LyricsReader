from LyricsReader import LyricsReader

if __name__ == '__main__':

    artist = 'THE BLUE HEARTS'
    title = '青空'

    objlyrics = LyricsReader(artist, title)
    
    if objlyrics.write_lyrics():
        print(f'歌詞『{title}』をテキストファイルに書き込みました。')

from GetLyrics import GetLyrics
from WriteLyrics import WriteLyrics

lyrics = ''
artist = '竹原ピストル'

#title = 'たった二種類の金魚鉢'
#title = 'ＯＮ　ＴＨＥ　ＲＯＡＤ'
#title = 'あっかんべ、だぜ故郷'
title = 'あ。っという間はあるさ'

objlyrics = GetLyrics(artist,title)

print(objlyrics.url)
print()

lyrics = objlyrics.text()

if lyrics:

    print(lyrics)
    print()

    if WriteLyrics(lyrics, '{}.txt'.format(title)).onTextFile():
        print('歌詞をテキストファイルに書き込みました。')

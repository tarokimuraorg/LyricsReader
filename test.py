from turtle import title
from GetLyrics import GetLyrics
from WriteLyrics import WriteLyrics

lyrics = ''
artist = '竹原ピストル'

#title = 'たった二種類の金魚鉢'
#title = 'ＯＮ　ＴＨＥ　ＲＯＡＤ'
#title = 'あっかんべ、だぜ故郷'
#title = 'あ。っという間はあるさ'
#title = 'いくぜ！いくか！いこうよ！'
#title = 'Amazing Grace' --- 取得エラー
#title = 'It\'s my life'
#title = '俺のアディダス～人としての志～ (Album ver.)'
title = 'オーバー・ザ・オーバー'

objlyrics = GetLyrics(artist,title)

print(objlyrics.url)
print()

lyrics = objlyrics.text()

if lyrics:

    print(lyrics)
    print()

    """
    if WriteLyrics('', '').onTextFile():
        print('歌詞をテキストファイルに書き込みました。')

    """
    
    if WriteLyrics(lyrics, 'lyrics/{}.txt'.format(title)).onTextFile():
        print('歌詞をテキストファイルに書き込みました。')

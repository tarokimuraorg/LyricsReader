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
#title = 'オーバー・ザ・オーバー'
#title = '俺、間違ってねえよな?'
#title = 'おーい！おーい！！'
#title = 'カウント10'
#title = 'きーぷ、うぉーきんぐ！！'
#title = 'Gimme the mic !!'
#title = '午前2時 私は今 自画像に描かれた自画像' --- 取得エラー
#title = '最期の一手 ～聖の青春～'
#title = '悄気る街、舌打ちのように歌がある。'
#title = 'STAY FREE!!'
#title = '全て身に覚えのある痛みだろう？'
#title = '高千穂峠のこいのぼり～ワルフザケガスギルMIX ～'
#title = 'ちぇっく！'
#title = '父から娘へ～さや侍の手紙～'
#title = 'テイク イット イージー'
#title = 'トム・ジョード'
#title = 'ドライブトライブ ～初代機材車、二郎号に捧ぐ～'
#title = 'どーん！とやってこい、ダイスケ！'
#title = '狼煙(朗読) ～Live at京都大作戦 2017～'
#title = 'Here we go!!'
#title = 'Float Like a Buttrefly, Sting Like a Bee!!'
#title = 'へっちゃらさ、ベイビー'
#title = '藍色のハンカチ '
title = ''

objlyrics = GetLyrics(artist,title)

print(objlyrics.url)
print()

lyrics = objlyrics.text()

if lyrics:

    """
    print(lyrics)
    print()
    """
    
    """
    if WriteLyrics('', '').onTextFile():
        print('歌詞をテキストファイルに書き込みました。')

    """
    
    if WriteLyrics(lyrics, 'lyrics/{}.txt'.format(title)).onTextFile():
        print('歌詞をテキストファイルに書き込みました。')

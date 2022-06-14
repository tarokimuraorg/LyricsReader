from turtle import title
from GetLyrics import GetLyrics
from WriteLyrics import WriteLyrics

artist = '竹原ピストル'

#title = '藍色のハンカチ'
#title = 'I miss you...'
#title = 'あっかんべ、だぜ故郷'
#title = 'あ。っという間はあるさ'
#title = 'Amazing Grace'
#title = 'いくぜ！いくか！いこうよ！'
#title = '石ころみたいにひとりぼっちで、命の底から駆け抜けるんだ'
#title = "It's my life"
#title = '一等賞'
#title = '笑顔でさよなら、跡形もなく。'
#title = '隠岐手紙'
#title = '奥底の歌'
#title = '朧月。君よ、今宵も生き延びろ。'
#title = '俺たちはまた旅に出た'
#title = '俺のアディダス～人としての志～ (Album ver.)'
#title = '俺、間違ってねえよな?'
#title = 'ON THE ROAD'
#title = 'おーい！おーい！！'
#title = 'オーバー・ザ・オーバー'
#title = 'オールドルーキー'
#title = 'カウント10'
#title = 'カモメ'
#title = '来た道戻るの大嫌い!'
#title = 'きーぷ、うぉーきんぐ！！'
#title = 'Gimme the mic !!'
#title = 'ギラギラなやつをまだ持ってる'
#title = 'ぐるぐる'
#title = '月光の仮面'
#title = '高円寺'
#title = '今宵もかろうじて歌い切る'
#title = '午前2時 私は今 自画像に描かれた自画像'
#title = 'ゴミ箱から、ブルース'
#title = '最期の一手 ～聖の青春～'
#title = 'サンサーラ'
#title = '3センチの歌'
#title = '悄気る街、舌打ちのように歌がある。'
#title = '辞世の句'
#title = 'じゅうじか'
#title = 'STAY FREE!!'
#title = '全て身に覚えのある痛みだろう？'
#title = 'せいぜい胸を張ってやるさ。'
#title = '高千穂峠のこいのぼり～ワルフザケガスギルMIX ～'
#title = 'ただ己が影を真似て'
#title = 'たった二種類の金魚鉢'
#title = '例えばヒロ、お前がそうだったように'
#title = 'ため息さかさにくわえて風来坊'
#title = 'ちぇっく！'
#title = '父から娘へ～さや侍の手紙～'
#title = '月夜をたがやせ'
#title = 'テイク イット イージー'
#title = '東京一年生'
#title = 'とまり木'
#title = 'トム・ジョード'
#title = 'ドサ回り数え歌'
#title = 'どっちみち どっちもどっちさ'
#title = 'ドライブトライブ ～初代機材車、二郎号に捧ぐ～'
#title = 'どーん！とやってこい、ダイスケ！'
#title = '夏のアウトロ コオロギの鳴く頃'
#title = 'なにもしないがしたい'
#title = '名も無き花'
#title = '虹は待つな 橋をかけろ'
#title = 'のらりくらり'
#title = '狼煙(朗読) ～Live at京都大作戦 2017～'
#title = '南十字星'
#title = 'ハッピーエンド'
#title = '初詣'
#title = 'ばかやろ。'
#title = 'Here we go!!'
#title = '一枝拝借 どこに生けるあてもなく'
#title = 'ひまわりさくまであとすこし'
#title = 'Forever Young'
#title = 'Float Like a Buttrefly, Sting Like a Bee!!'
#title = 'へっちゃらさ、ベイビー'
#title = '本庄のド根性'
#title = 'ぼくの夢でした'
#title = 'ぼくは限りない～One for the show～'
#title = 'my dear'
#title = 'マイメン'
#title = 'Mother'
#title = 'マスター、ポーグスかけてくれ'
#title = 'ママさんそう言った ～Hokkaido days～'
#title = '未完成'
#title = '御幸橋'
#title = 'みんな～、やってるか!'
#title = 'youth'
#title = 'よー、そこの若いの'
#title = 'LIVE IN 和歌山'
#title = 'リョウジ'
#title = 'リョウメンシダ'
#title = 'ルート トゥ ルーツ'
#title = 'RAIN'
title = 'わたしのしごと'

objlyrics = GetLyrics(artist,title)

print(objlyrics.url)
print()

lyrics = objlyrics.text()

if lyrics:

    if WriteLyrics(lyrics, 'lyrics/{}.txt'.format(title)).onTextFile():
        print('歌詞 : {} をテキストファイルに書き込みました。'.format(title))
    else:
        print('テキストファイルの出力に失敗しました。（歌詞 : {}）'.format(title))

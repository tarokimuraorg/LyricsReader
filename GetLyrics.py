import requests
from bs4 import BeautifulSoup
import urllib
import re
from ErrorMessageCreator import ErrorMessageCreator
from StringConvertor import StringConvertor

class GetLyrics:

    def __init__(self, artist : str, title : str):

        self.url = ''

        out_artist = artist.strip()
        out_title = title.strip()

        strconvertor = StringConvertor()

        if out_artist and out_title:
            
            out_artist = out_artist.replace('.',' ')
            out_artist = out_artist.replace('!', ' ')
            out_artist = out_artist.replace('！', ' ')
            out_artist = out_artist.replace('。', ' ')
            out_artist = out_artist.replace('、', ' ')
            out_artist = out_artist.replace(',', ' ')
            out_artist = out_artist.replace('~', ' ')
            out_artist = out_artist.replace('～', ' ')
            out_artist = out_artist.replace('(', ' ')
            out_artist = out_artist.replace(')', ' ')
            out_artist = out_artist.replace('（', ' ')
            out_artist = out_artist.replace('）', ' ')
            out_artist = out_artist.replace('・', ' ')
            out_artist = out_artist.replace('　', ' ')
            out_artist = out_artist.replace('?', ' ')
            out_artist = out_artist.replace('？', ' ')
            out_artist = re.sub(' +',' ',out_artist)
            out_artist = strconvertor.toHankaku(out_artist)
            out_artist = out_artist.strip()
            
            list_artist = out_artist.split(' ')
            list_artist = list(map(lambda a: urllib.parse.quote(a), list_artist))

            out_artist = '+'.join(list_artist)
            
            out_title = out_title.replace('.',' ')
            out_title = out_title.replace('!', ' ')
            out_title = out_title.replace('！', ' ')
            out_title = out_title.replace('。', ' ')
            out_title = out_title.replace('、', ' ')
            out_title = out_title.replace(',', ' ')
            out_title = out_title.replace('~', ' ')
            out_title = out_title.replace('～', ' ')
            out_title = out_title.replace('(', ' ')
            out_title = out_title.replace(')', ' ')
            out_title = out_title.replace('（', ' ')
            out_title = out_title.replace('）', ' ')
            out_title = out_title.replace('・', ' ')
            out_title = out_title.replace('　',' ')
            out_title = out_title.replace('?', ' ')
            out_title = out_title.replace('？', ' ')
            out_title = re.sub(' +',' ',out_title)
            out_title = strconvertor.toHankaku(out_title)
            out_title = out_title.strip()

            list_title = out_title.split(' ')
            list_title = list(map(lambda t: urllib.parse.quote(t), list_title))

            out_title = '+'.join(list_title)

            url = 'https://www.google.com/search?q='
            url = url + urllib.parse.quote('歌詞')
            url = url + '+'
            url = url + out_artist
            url = url + '+'
            url = url + out_title

            self.url = url

        self.__emcreator = ErrorMessageCreator()

    def text(self) -> str:

        try:

            if self.url:

                response = requests.get(self.url)
                response.raise_for_status()
                response.encoding = response.apparent_encoding

                soup = BeautifulSoup(response.text, 'html.parser')
                data = soup.find_all('div',class_='hwc')

                result = ''

                for d in data:
                    result += d.text

                result = result.strip()

                if result:
                    return result.strip()
            
                raise ValueError(self.__emcreator.message('GetLyrics','text','取得エラー','取得したデータが空です。'))

            else:
                raise ValueError(self.__emcreator.message('GetLyrics','init','引数エラー','アーティスト名 または 曲のタイトルが入力されていません。'))

        except requests.exceptions.RequestException:
            print('{}'.format(self.__emcreator.message('GetLyrics','text','通信エラー','データの取得に失敗しました。')))
            return ''
            
        except ValueError as e:
            print('{}'.format(e))
            return ''

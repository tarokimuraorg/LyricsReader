import os
import urllib
import re
import requests
from bs4 import BeautifulSoup
from ErrorMessageCreator import ErrorMessageCreator
from StringConvertor import StringConvertor

class LyricsReader:

    def __init__(self, artist : str, title : str):

        self.__url = ''
        self.__path = ''

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
            out_artist = out_artist.replace('?', ' ')
            out_artist = out_artist.replace('？', ' ')
            out_artist = out_artist.replace('・',' ')
            out_artist = out_artist.replace('　', ' ')
            out_artist = re.sub(' +',' ',out_artist)
            out_artist = strconvertor.toHankaku(out_artist)
            out_artist = out_artist.strip()
            
            list_artist = out_artist.split(' ')
            list_artist = list(map(lambda item: urllib.parse.quote(item), list_artist))

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
            out_title = out_title.replace('?', ' ')
            out_title = out_title.replace('？', ' ')
            out_title = out_title.replace('・', ' ')
            out_title = out_title.replace('　',' ')
            out_title = re.sub(' +',' ',out_title)
            out_title = strconvertor.toHankaku(out_title)
            out_title = out_title.strip()

            out_path = 'lyrics'
            os.makedirs(out_path, exist_ok=True)

            self.__path = '{}/{}.txt'.format(out_path, out_title.replace(' ', '_'))

            list_title = out_title.split(' ')
            list_title = list(map(lambda item: urllib.parse.quote(item), list_title))

            out_title = '+'.join(list_title)

            url = 'https://www.google.com/search?q='
            url = url + urllib.parse.quote('歌詞')
            url = url + '+'
            url = url + out_artist
            url = url + '+'
            url = url + out_title

            self.__url = url

        self.__emcreator = ErrorMessageCreator()

    def read_lyrics(self) -> str:

        try:

            if self.__url:

                response = requests.get(self.__url)
                response.raise_for_status()
                response.encoding = response.apparent_encoding

                soup = BeautifulSoup(response.text, 'html.parser')
                
                data = soup.find_all('div', class_='hwc')

                result = ''

                for d in data:

                    result += d.text
                    result += '\n'

                result = result.strip()

                if result:
                    return result.strip()

                data = soup.find_all('div', class_='BNeawe tAd8D AP7Wnd')

                line = ''
                result = ''

                arr_result = []
                arr_line = []
                
                for d in data:

                    line = d.text.strip()
                    arr_line = line.split('\n')
                    
                    if len(arr_result) < len(arr_line):
                        result = line
                        arr_result = arr_line
                    
                if result:
                    return result

                print(self.__emcreator.message('LyricsReader','read_lyrics','取得エラー','取得したデータが空です。'))
                return ''

            else:
                print(self.__emcreator.message('LyricsReader','init','引数エラー','アーティスト名 または 曲のタイトルが入力されていません。'))
                return ''

        except requests.exceptions.RequestException:

            print(self.__emcreator.message('LyricsReader','read_lyrics','通信エラー','データの取得に失敗しました。'))
            return ''
            
        except ValueError as ve:

            print(f'{ve}')
            return ''

    def write_lyrics(self) -> bool:

        out_lyrics = self.read_lyrics()

        if out_lyrics:

            try:

                with open(self.__path, 'x', encoding='UTF-8') as f:

                    f.write(out_lyrics)
                    f.close()
                    
                return True

            except FileExistsError as e:

                print(self.__emcreator.message('LyricsReader','write_lyrics','書き込みエラー','指定したファイル名はすでに存在しています。'))
                return False

            except ValueError as e:

                print(f'{e}')
                return False

        else:
            return False

import requests
from bs4 import BeautifulSoup
import urllib
import re
from ErrorMessageCreator import ErrorMessageCreator

class GetLyrics:

    def __init__(self, artist : str, title : str):

        out_artist = artist.strip()
        out_artist = re.sub('　+',' ',out_artist)
        out_artist = re.sub(' +',' ',out_artist)
        out_artist = urllib.parse.quote(out_artist)

        out_title = title.strip()
        out_title = re.sub('　+',' ',out_title)
        out_title = re.sub(' +',' ',out_title)
        out_title = urllib.parse.quote(out_title)

        url = 'https://www.google.com/search?q='
        url = url + urllib.parse.quote('歌詞')
        url = url + '+'
        url = url + out_artist
        url = url + '+'
        url = url + out_title

        self.url = url
        self._emcreator = ErrorMessageCreator()

    def text(self) -> str:
        
        try:
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
            
            raise ValueError(self._emcreator.message('GetLyrics','text','取得エラー','取得したデータが空です。'))

        except requests.exceptions.RequestException as e:
            print('{}'.format(self._emcreator.message('GetLyrics','text','通信エラー','{}}'.format(e))))
        
        except ValueError as e:
            print('{}'.format(e))

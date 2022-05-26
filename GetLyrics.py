import requests
from bs4 import BeautifulSoup
import urllib

class GetLyrics:

    def __init__(self, artist : str, title : str):

        self.__artist = urllib.parse.quote(artist)
        self.__title = urllib.parse.quote(title)

    def text(self) -> str:
        
        url = 'https://www.google.com/search?q='
        url = url + urllib.parse.quote('歌詞')
        url = url + '+'
        url = url + self.__artist
        url = url + '+'
        url = url + self.__title

        response = requests.get(url)
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('div',class_='hwc')

        result = ''

        for d in data:
            result += d.text

        return result.strip()

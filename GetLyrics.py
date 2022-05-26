import requests
from bs4 import BeautifulSoup
import urllib

class GetLyrics:

    def __init__(self, artist : str, title : str):

        self.__artist = artist.strip()
        self.__artist = self.__artist.replace(' ', '+')
        self.__artist = self.__artist.replace('　', '+')
        self.__artist = urllib.parse.quote(self.__artist)

        self.__title = title.strip()
        self.__title = self.__title.replace(' ', '+')
        self.__title = self.__title.replace('　', '+')
        self.__title = urllib.parse.quote(self.__title)

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

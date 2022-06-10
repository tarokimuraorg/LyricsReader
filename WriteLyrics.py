import re
from ErrorMessageCreator import ErrorMessageCreator

class WriteLyrics:

    def __init__(self, lyrics : str, path : str):

        self.__path = ''
        self.__lyrics = ''

        out_path = path.strip()
        out_lyrics = lyrics.strip()

        if out_path and out_lyrics:

            out_path = out_path.replace('?', ' ')
            out_path = out_path.replace('？', ' ')
            out_path = out_path.replace('　', ' ')
            out_path = out_path.replace('、', ' ')
            out_path = out_path.replace(',', ' ')
            out_path = out_path.replace('(', ' ')
            out_path = out_path.replace(')', ' ')
            out_path = out_path.replace('（', ' ')
            out_path = out_path.replace('）', ' ')
            out_path = out_path.replace('!', ' ')
            out_path = out_path.replace('！', ' ')
            out_path = out_path.replace('。', ' ')
            out_path = out_path.replace('～', ' ')
            out_path = out_path.replace('~', ' ')
            out_path = out_path.replace('.', ' ')
            out_path = out_path.replace('・', ' ')
            out_path = out_path.strip()

            out_path = re.sub(' +', '_', out_path)
            
            if re.search('_txt$', out_path) is None:
                out_path = '{}.txt'.format(out_path)
            else:
                out_path = re.sub('_txt$', '.txt', out_path)

            self.__path = out_path
            self.__lyrics = out_lyrics

        self.__emcreator = ErrorMessageCreator()

    def onTextFile(self) -> bool:

        try:

            if self.__path and self.__lyrics:

                with open(self.__path, 'x', encoding='UTF-8') as f:

                    f.write(self.__lyrics)
                    f.close()
            
                return True

            else:
                raise ValueError(self.__emcreator.message('WriteLyrics','init','引数エラー','出力するテキストファイルのパス または 歌詞が入力されていません。'))

        except FileExistsError as e:

            print(self.__emcreator.message('WriteLyrics','onTextFile','書き込みエラー','指定したファイル名はすでに存在しています。'))
            return False

        except ValueError as e:

            print('{}'.format(e))
            return False

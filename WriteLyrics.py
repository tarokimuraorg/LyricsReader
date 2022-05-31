import re
from ErrorMessageCreator import ErrorMessageCreator

class WriteLyrics:

    def __init__(self, lyrics : str, file_name : str):
        
        out_file_name = file_name.strip()

        if out_file_name:
            out_file_name = 'no_title.txt'

        else:

            out_file_name = re.sub('　+', ' ', out_file_name)
            out_file_name = re.sub(' +', '_', out_file_name)

            if re.search('.txt$', out_file_name) is None:
                out_file_name = '{}.txt'.format(out_file_name)

        self.__file_name = out_file_name
        self.__lyrics = lyrics
        self.__emcreator = ErrorMessageCreator()

    def onTextFile(self) -> bool:

        try:

            with open(self.__file_name, 'x', encoding='UTF-8') as f:
                f.write(self.__lyrics)
                f.close()
            
            return True

        except FileExistsError as e:

            print(self.__emcreator.message('WriteLyrics','onTextFile','書き込みエラー','指定したファイル名はすでに存在しています。'))
            return False

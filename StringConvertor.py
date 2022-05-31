class StringConvertor:

    def __init__(self):

        self.__zenkaku_data = [0xff01 + i for i in range(94)]
        self.__hankaku_data = [0x21 + i for i in range(94)]        

    def toHankaku(self, zenkaku : str) -> str:

        data = {self.__zenkaku_data[i]:self.__hankaku_data[i] for i in range(94)}
        return zenkaku.translate(data)

    def toZenkaku(self, hankaku : str) -> str:

        data = {self.__hankaku_data[i]:self.__zenkaku_data[i] for i in range(94)}
        return hankaku.translate(data)

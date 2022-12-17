'''
    词典
'''
class Dictionary:

    
    def __init__(self):
        self.wordMap = {}
    
    '''
        添加一个词项
    '''
    def addItem(self, item):
        self.wordMap[item.value] = item    

    '''
        统计词典中的单词数量
    '''
    def count(self):
        return len(self.wordMap.keys())

    '''
        查询
    '''
    def query(self, value):
        return self.wordMap.get(value)

    '''
        判断 value 是否在词典中
    '''
    def exist(self, value):
        return self.query(value) is not None
    

'''
    词项
'''
class Item:

    def __init__(self, value, count, types):
        self.value = value
        self.count = count
        self.types = types

    def __str__(self):
        return '{} {} {}'.format(self.value, self.count, self.types)




class DictionaryLoader:

    DICT_TXT_BIG = '/home/anyang/project/learnlp/data/dict.txt.big'

    @staticmethod
    def load():
        dict = Dictionary()
        with open(DictionaryLoader.DICT_TXT_BIG) as reader:
            while True:
                line = reader.readline()
                if line is None or len(line) == 0:
                    break
                item = DictionaryLoader.parse(line)
                if item is None:
                    continue
                dict.addItem(item)
            
        return dict

    @staticmethod
    def parse(line):
        list = line.split(' ')
        if len(list) != 3:
            print('解析词项出错: {}'.format(line))
        value = list[0]
        count = list[1]
        types = list[2]
        return Item(value, count, types)


dictionary = DictionaryLoader.load()
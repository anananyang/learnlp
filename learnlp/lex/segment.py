from abc import ABCMeta, abstractmethod
from dict.dictionary import dictionary

class Segment(metaclass=ABCMeta):
    
    @abstractmethod
    def cut(self, str):
        pass


'''完全切分算法'''
class FullySegment(Segment):

    def cut(self, str):
        if str is None or len(str) == 0:
            return None
        words = []
        strlen = len(str)
        for i in range(strlen + 1):
            j = i
            for j in range(strlen + 1):
                word = str[i:j]
                if dictionary.exist(word):
                    words.append(word)

        return words


'''正向最长匹配'''



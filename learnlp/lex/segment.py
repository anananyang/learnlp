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
class HmmSegment(Segment):

    def cut(self, str):
        if str is None or len(str) == 0:
            return None
        words = []
        strlen = len(str) 
        base = 0
        while base < strlen:
            j = base
            mm_word = None
            for j in (range(strlen + 1)):
                word = str[base:j]
                if dictionary.exist(word):
                    if mm_word is None or len(mm_word) < len(word):
                        mm_word = word
            if mm_word is not None:
                words.append(mm_word)
                base = base + len(mm_word)
            else:
                base = base + 1      
        return words

'''逆向最长匹配'''
class BmmSegment(Segment):
    def cut(self, str):
        pass


'''双向最长匹配'''
class TwoWaymmSegment(Segment):
    def cut(self, str):
        pass

from abc import ABCMeta, abstractmethod
from dict.dictionary import dictionary

class Segment(metaclass=ABCMeta):
    
    @abstractmethod
    def cut(self, str):
        pass

    @abstractmethod
    def desc(self):
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

    def desc(self):
        return '完全切分算法'
    
    


'''正向最长匹配'''
class HmmSegment(Segment):

    def cut(self, str):
        if str is None or len(str) == 0:
            return None
        words = []
        strlen = len(str) 
        base = 0
        while base < strlen:
            j = base + 1
            mm_word = None
            while j <= strlen:
                word = str[base:j]
                if dictionary.exist(word):
                    mm_word = word
                j = j + 1
            if mm_word is not None:
                words.append(mm_word)
                base = base + len(mm_word)
            else:
                base = base + 1      
        return words


    def desc(self):
        return '正向最长匹配'

'''逆向最长匹配'''
class BmmSegment(Segment):
    def cut(self, str):
        if str is None or len(str) == 0:
            return None
        words = []
        base = len(str)
        while base > 0:
            j =  base - 1
            mm_word = None
            while j >= 0:
                word = str[j:base]
                if dictionary.exist(word):
                    mm_word = word
                j = j - 1
                
            if mm_word is not None:
                base = base - len(mm_word)
                words.insert(0, mm_word)
            else:
                base = base - 1
        return words

    
    def desc(self):
        return '逆向最长匹配'

        

'''双向最长匹配'''
class TwoWaymmSegment(Segment):
    def __init__(self):
        self.hmmSegment = HmmSegment()
        self.bmmSegment = BmmSegment()

    def cut(self, str):
        if str is None or len(str) == 0:
            return None
        hmm_words = self.hmmSegment.cut(str)
        bmm_words = self.bmmSegment.cut(str)
        '''返回单词数量最少的结果'''
        words = self.__get_min_len_words(hmm_words, bmm_words)
        if words is not None:
            return words
        '''如果单词数量相等，则返回只有一个字的单词数量最少的结果'''
        words = self.__get_min_single_words(hmm_words, bmm_words)
        if words is not None:
            return words
        ''''如果以上都一样，则返回逆向最长匹配的结果'''
        return bmm_words

    def  __get_min_len_words(self, hmm_words, bmm_words):
        hmm_words_len = len(hmm_words)
        bmm_words_len = len(bmm_words)
        if hmm_words_len < bmm_words_len:
            return hmm_words
        elif  hmm_words_len > bmm_words_len:
            return bmm_words
        else:
            return None

    def __get_min_single_words(self, hmm_words, bmm_words):
        hmm_single_world_len = self.__count_single_word(hmm_words)
        bmm_single_world_len = self.__count_single_word(bmm_words)
        if hmm_single_world_len < bmm_single_world_len:
            return hmm_words
        elif  hmm_single_world_len > bmm_single_world_len:
            return bmm_words
        else:
            return None

    def __count_single_word(self, words):
        if words is None :
            return 0
        count = 0
        for word in words:
            if len(word) == 1:
                count = count + 1
        return count;

    def desc(self):
        return '双向最长匹配'



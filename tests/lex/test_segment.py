import unittest
import tests.context
from learnlp.lex.segment import FullySegment 


class TestSegment(unittest.TestCase):
    
    '''测试完全切分算法'''
    def test_fully_segment(self):
        # arrange
        str = "今天是星期五"
        segment = FullySegment()
        # act
        words = segment.cut(str)
        # assert
        self.assertTrue(len(words) > 0)




if __name__ == '__main__':
    unittest.main()




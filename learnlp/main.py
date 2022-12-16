from lex.segment import FullySegment
from lex.segment import HmmSegment
from lex.segment import BmmSegment
from lex.segment import TwoWaymmSegment

str = '我想搭个顺风车'

def fully_segment():
    segment = FullySegment()
    words = segment.cut(str)
    print(words)

def hmm_segment():
    segment = HmmSegment()
    words = segment.cut(str)
    print(words)

def bmm_segment():
    segment = BmmSegment()
    words = segment.cut(str)
    print(words)

def two_way_mm_segment():
    segment = TwoWaymmSegment()
    words = segment.cut(str)
    print(words)


def main():
#    fully_segment()
   hmm_segment()
#    bmm_segment()
#    two_way_mm_segment()

    
if __name__ == '__main__':
    main()

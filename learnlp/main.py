from lex.segment import FullySegment
from lex.segment import HmmSegment
from lex.segment import BmmSegment
from lex.segment import TwoWaymmSegment

strs = ['我想搭个顺风车', '研究生命起源', '项目的研究']

def fully_segment():
    print('----------------------- 完全切分 ------------------------')
    segment = FullySegment()
    for str in strs:
        words = segment.cut(str)
        print(f'{str} 结果：{words}')
    print('\n')

def hmm_segment():
    print('----------------------- 正向最长匹配 ------------------------')
    segment = HmmSegment()
    for str in strs:
        words = segment.cut(str)
        print(f'{str} 结果：{words}')
    print('\n')
    
def bmm_segment():
    print('----------------------- 逆向最长匹配 ------------------------')
    segment = BmmSegment()
    for str in strs:
        words = segment.cut(str)
        print(f'{str} 结果：{words}')
    print('\n')

def two_way_mm_segment():
    print('----------------------- 双向最长匹配 ------------------------')
    segment = TwoWaymmSegment()
    for str in strs:
        words = segment.cut(str)
        print(f'{str} 结果：{words}')
    print('\n')


def main():
   fully_segment()
   hmm_segment()
   bmm_segment()
   two_way_mm_segment()

    
if __name__ == '__main__':
    main()
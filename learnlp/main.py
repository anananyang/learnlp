from lex.segment import FullySegment
from lex.segment import HmmSegment
from lex.segment import BmmSegment
from lex.segment import TwoWaymmSegment
from accuracy.accurate import Accurator

strs = ['我想搭个顺风车', '研究生命起源', '项目的研究']
golds = [
    ['我', '想', '搭', '个', '顺风车'],
    ['研究', '生命', '起源'],
    ['项目', '的', '研究']
]

def segment(segment):
    if segment is None:
        return
    print(f'----------------------- {segment.desc()} ------------------------')
    accurator = Accurator()
    for str, gold in zip(strs, golds):
        pred = segment.cut(str)
        p, r, f = accurator.accurate(gold, pred)
        print(f'{str} 结果：{pred}。准确率: p = {p}, 召回率 r={r}, f={f}')
    print('\n')

def fully_segment():
   segment(FullySegment())

def hmm_segment():
    segment(HmmSegment())
    
def bmm_segment():
    segment(BmmSegment())

def two_way_mm_segment():
    segment(TwoWaymmSegment())

def main():
   fully_segment()
   hmm_segment()
   bmm_segment()
   two_way_mm_segment()

    
if __name__ == '__main__':
    main()
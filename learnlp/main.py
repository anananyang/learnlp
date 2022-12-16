from lex.segment import FullySegment


def main():
    str = '我想搭个顺风车'
    segment = FullySegment()
    words = segment.cut(str)
    print(words)
    
if __name__ == '__main__':
    main()

class Accurator:

    def __init__(self):
        pass

    '''
        准确率计算
        :param gold: 准确的结果
        :param pred: 预测的结果
        :return: p、r、f，其中 p 表示准确率、r 表示召回率
    '''
    def accurate(self, gold, pred):
        gold_region = self.__to_region(gold)
        pred_region = self.__to_region(pred)
        same_num = self.__calc_same_num(gold_region, pred_region)
        p = round(same_num / len(pred_region), 2)
        r = round(same_num / len(gold_region), 2)
        f = round((2 * p * r) / (p + 1), 2)
        return p, r, f


    def __to_region(self, words):
        region = []
        start  = 0
        for word in words:
            end = start + len(word)
            region.append((start, end))
            start =+ end
        return region

    def __calc_same_num(self, gold_region, pred_region):
        same = 0
        for region in pred_region:
            if gold_region.count(region) > 0:
                same += 1
        
        return same
def score(tp = 2, fp = 3, fn = 4):
    '''
    This function aims to calculate classification measure like Precision, Recall and F1-score.

    Inputs:
        tp (int): True positive count,
        fp (int): False positive count,
        fn (int): False negative count.
    
    Output:
        None: Print the calculated precision, recall, and F1-score.
    '''
    if type(tp) != int:
        print('tp must be int')
        return
    if type(fp) != int:
        print('fp must be int')
        return
    if type(fn) != int:
        print('fn must be int')
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1_score is {f1_score}')
    return 
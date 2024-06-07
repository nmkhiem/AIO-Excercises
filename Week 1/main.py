import activation_func, approx_function, classification_score, loss_function, md_nre

if __name__ == '__main__':
    print('Ex1: ')
    classification_score.score(tp = 2, fp = 3, fn = 5)
    # classification_score.score(tp = 0, fp = 3, fn = 4)
    # classification_score.score(tp = 'a', fp = 3, fn = 4)
    # classification_score.score(tp = 0, fp = 3, fn = 'a')

    print('Ex2: ')
    activation_func.count_activation()

    print('Ex3:')
    loss_function.loss()

    print('Ex4:')
    print(approx_function.approx_sin(x = 3.14, n = 10))
    # print(approx_function.approx_cos(x = 3.14, n = 10))
    # print(approx_function.approx_sinh(x = 3.14, n = 10))
    # print(approx_function.approx_cosh(x = 3.14, n = 10))

    print('Ex5:')
    print(md_nre.md_nre(y = 100, y_hat = 99.5, n = 2, p = 1))
    # print(md_nre.md_nre(y = 20, y_hat = 19.5, n = 2, p = 1))

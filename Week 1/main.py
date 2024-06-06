import Ex1, Ex2, Ex3, Ex4, Ex5

if __name__ == '__main__':
    print('Ex1: ')
    Ex1.score(tp = 2, fp = 3, fn = 4)
    # Ex1.score(tp = 0, fp = 3, fn = 4)
    # Ex1.score(tp = 'a', fp = 3, fn = 4)
    # Ex1.score(tp = 0, fp = 3, fn = 'a')

    print('Ex2: ')
    Ex2.count_activation()

    print('Ex3:')
    Ex3.loss()

    print('Ex4:')
    print(Ex4.approx_sin(x = 3.14, n = 10))
    # print(Ex4.approx_cos(x = 3.14, n = 10))
    # print(Ex4.approx_sinh(x = 3.14, n = 10))
    # print(Ex4.approx_cosh(x = 3.14, n = 10))

    print('Ex5:')
    print(Ex5.md_nre(y = 100, y_hat = 99.5, n = 2, p = 1))
    print(Ex5.md_nre(y = 20, y_hat = 19.5, n = 2, p = 1))

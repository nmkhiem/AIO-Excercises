import activation_func, approx_function, classification_score, loss_function, md_nre

if __name__ == '__main__':
    print('Ex1: ')
    classification_score.score(tp = 2, fp = 3, fn = 5)

    print('Ex2: ')
    activation_func.count_activation()

    print('Ex3:')
    loss_function.loss()

    print('Ex4:')
    print(approx_function.approx_sin(x = 3.14, n = 10))

    print('Ex5:')
    print(md_nre.md_nre(y = 100, y_hat = 99.5, n = 2, p = 1))

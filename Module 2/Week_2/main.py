import numpy as np
import dot_product

if __name__ == '__main__':
    print("Ex 1: ")
    vector = np. array([-2, 4, 9, 21])
    result = dot_product.compute_vector_length([vector])
    print(round(result, 2))

    print("Ex 2: ")
    v1 = np. array([0, 1, -1, 2])
    v2 = np. array([2, 5, 1, 0])
    result = dot_product.compute_dot_product(v1, v2)
    print(round(result, 2))

    print("Ex 3: ")
    x = np. array([[1, 2], [3, 4]])
    k = np. array([1, 2])
    print('result \n', x.dot(k))

    print("Ex 4: ")
    x = np. array([[-1, 2],
                   [3, -4]])
    k = np. array([1, 2])
    print('result \n', x@k)

    print("Ex 5: ")
    m = np. array([[-1, 1, 1], [0, -4, 9]])
    v = np. array([0, 2, 1])
    result = dot_product.matrix_multi_vector(m, v)
    print(result)

    print("Ex 6: ")
    m1 = np. array([[0, 1, 2], [2, -3, 1]])
    m2 = np. array([[1, -3], [6, 1], [0, -1]])
    result = dot_product.matrix_multi_matrix(m1, m2)
    print(result)

    print("Ex 7: ")
    m1 = np.eye(3)
    m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    result = m1@m2
    print(result)

    print("Ex 8: ")
    m1 = np.eye(2)
    m1 = np. reshape(m1, (-1, 4))[0]
    m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    print("Ex 9: ")
    m1 = np. array([[1, 2], [3, 4]])
    m1 = np. reshape(m1, (-1, 4), "F")[0]
    m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    print("Ex 10: ")
    m1 = np. array([[-2, 6], [8, -4]])
    result = dot_product.inverse_matrix(m1)
    print(result)

    print("Ex 11: ")
    matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues, eigenvectors = dot_product.compute_eigenvalues_eigenvectors(
        matrix)
    print(eigenvectors)

    print("Ex 12: ")
    x = np. array([1, 2, 3, 4])
    y = np. array([1, 0, 3, 0])
    result = dot_product.compute_cosine(x, y)
    print(round(result, 3))

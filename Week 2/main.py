import sliding_window
import count_chars
import word_count
import edit_distance

if __name__ == '__main__':
    print('Ex1 :')
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    max_list = sliding_window.sliding_window(num_list, k)

    print('Max list :', max_list)

    print('Ex2 :')
    string = 'Happiness'
    dictionary = count_chars.count_chars(string)
    print('Dictionary :', dictionary)

    print('Ex3 :')
    with open('C:/Users/84909/Documents/GitHub/Git - Demo/AIO-Excercises/Week 2/P1_data.txt', "r") as file:
        data = file.read()
    print(data)
    print(word_count.word_count(data))

    print('Ex4 :')
    str1 = 'kitten'
    str2 = 'sitting'
    optimal_distance = edit_distance.edit_distance(str1, str2)
    print('Optimal distance: ', optimal_distance)

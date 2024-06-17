def count_chars(string):
    dictionary = {}

    for c in string:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    keys = list(dictionary.keys())
    keys.sort()
    sorted_dict = {i: dictionary[i] for i in keys}
    return sorted_dict

def sliding_window(num_list, k):
    max_list = []
    n = len(num_list)
    for i in range(n-2):
        sub_list = num_list[i:i+k]
        max_number = max(sub_list)
        max_list.append(max_number)

    return max_list

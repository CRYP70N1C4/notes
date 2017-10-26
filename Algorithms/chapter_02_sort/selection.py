
'''
选择排序
'''
def sort(data):
    if not isinstance(data, list):
        return data
    for i in range(len(data)):
        min = i
        for j in range(i + 1, len(data)):
            if (data[min] > data[j]):
                min = j;
        data[i], data[min] = data[min], data[i]
    return data


if __name__ == '__main__':
    data = [21, 42, 5, 6, 7, 10, 20]
    print(data)
    print(sort(data))

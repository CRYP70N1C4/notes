'''
快速排序
'''

def sort(data, lo=0, hi=-1):
    if not isinstance(data, list) or len(data) == 1:
        return data
    if hi == -1:
        hi = len(data) - 1
    if lo >= hi:
        return data
    base = data[lo]
    lo1 = lo
    hi1 = hi
    while hi > lo:
        while data[hi] >= base and hi > lo:
            hi -= 1
        while data[lo] <= base and lo < hi:
            lo += 1
        if hi != lo:
            data[hi], data[lo] = data[lo], data[hi]
    data[lo1], data[hi] = data[hi], data[lo1]
    sort(data, lo1, lo - 1)
    sort(data, lo + 1, hi1)
    return data


if __name__ == '__main__':
    data = [21, 42, 5, 6, 7, 10, 20]
    print(data)
    print(sort(data))

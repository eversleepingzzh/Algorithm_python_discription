def binary_search(list, item):
    low = 0
    high = len(list)  # list中元素的数目

    while low <= high:
        mid = int((low + high) / 2)  # 取中间元素的
        guess = list[mid]
        if guess == item:  # 如果列表中间的元素是要找的数字，返回的mid为查找的次数
            return mid
        elif guess > item:
            high = mid - 1  # 如果中间元素比目标数字大，则以此时的中间元素的前一位为high
        else:
            low = mid + 1  # 如果中间元素比目标数字小，则以此时的中间元素的后一位为low
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 1))



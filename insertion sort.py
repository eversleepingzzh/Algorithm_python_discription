def insertion_sort(A):
    for j in range(1, len(A)):  # 假设第一个数是排序好的
        key = A[j]  # 取出当前未排序的数
        i = j - 1  # 从后往前，先取未排序数的前一个数（已经排序好的数）
        while i >= 0 and A[i] > key:  # 若当前未排序的数比排序好的数还小 并且没有到数组的开头
            A[i + 1] = A[i]  # 排序好的数往后挪一个位置
            i = i - 1  # 取排序好的数的前一个数进行比较
        A[i + 1] = key  # 插入当前要排序的数


arr = [5, 6, 2, 7, 9, 0, 1, 3, 8, 4]
insertion_sort(arr)
print(arr)
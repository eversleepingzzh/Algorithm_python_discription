def insertion_sort(list):
    n = len(list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
            else:
                break
    return list

arr = [5, 6, 2, 7, 9, 0, 1, 3, 8, 4]
insertion_sort(arr)
print(arr)
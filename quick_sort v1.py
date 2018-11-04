def quick_sort(A, p, r):
    q = partion(A, p, r)
    quick_sort(A, p, q - 1)
    quick_sort(A, q, r)

def partion(A, p ,r):
    x = A[r]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A [r]
    return i + 1



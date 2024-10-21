def mergeSort(a):
    if len(a)==1:
        return a
    medio=len(a)//2
    left = mergeSort(a[:medio])
    right = mergeSort(a[medio:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Agregar los elementos restantes de left y right
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


a=[4,2,7,9,1,23,4,6,22,14]
print(mergeSort(a))
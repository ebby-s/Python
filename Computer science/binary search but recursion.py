def search(array,target):
    Current = int(len(array)/2)
    if array[Current] == target: return Current
    elif target > array[Current]: return Current + search(array[Current:],target)
    else: return search(array[:Current],target)

array = [1,4,6,9,13,15,17,21,24,28,32,36,42,62,72,95,103,115]
print(search(array,62))

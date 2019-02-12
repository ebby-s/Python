import datetime,random

def sort(array):
    for i,CurrentValue in enumerate(array[1:]):
        for pos,elem in enumerate(array):
            if elem >= CurrentValue:
                del(array[i+1])
                array.insert(pos,CurrentValue)
                break
    return array

def checked_sort(array):
    for i,CurrentValue in enumerate(array[1:]):
        for pos,elem in enumerate(array):
            if elem >= CurrentValue:
                del(array[i+1])
                array.insert(pos,CurrentValue)
                break
        if is_sorted(array): break
    return array

def is_sorted(array):
    for i in range(len(array)):
        if len(array)-1 == i: break
        elif array[i] > array[i+1]: return False
    return True

def test(sort):
    unsorted = [random.randint(0,255) for x in range(20)]
    start = datetime.datetime.now()
    sort(unsorted)
    end = datetime.datetime.now()
    return (end-start).microseconds


times = [test(sort) for x in range(20000)]
avg = sum(times)/len(times)
print(avg)

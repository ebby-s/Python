
unsorted = [6,3,11,4,97,23,10,45,37,26,2,7,3]

def insertion_sort(unsorted):
    for i in range(1,len(unsorted)):    # Goes through list, starting from the second value
        CurrentValue = unsorted[i]
        for pos in range(len(unsorted)):       # Compares the current value to each element in the list
            if CurrentValue > unsorted[pos]:
                continue
            else:                           # Insert the value into the list
                del(unsorted[i])
                unsorted.insert(pos,CurrentValue)
                break
    return unsorted

sort = insertion_sort(unsorted)

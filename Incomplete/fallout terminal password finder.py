

def filter(term,likeness,word_list):
    filtered_list = []
    for word in word_list:
        c_likeness = 0
        for i in range(len(term)):
            if term[i] == word[i]:
                c_likeness += 1
        if c_likeness == likeness:
            filtered_list.append(word)
    return filtered_list


def get_num_words(str): 
    return len(str.split())

def count_characters(str): 
    new_str = list(str.lower())
    letter_count = {}
    for char in new_str: 
        if char not in letter_count: 
            letter_count[char] = 1
        else: 
            letter_count[char] += 1

    return letter_count

def list_of_dicts(dict): 
    list_d = []
    for i, j in dict.items(): 
        list_d.append({'char': i, 'count': j})
    
    list_d.sort(reverse=True, key= (lambda x: x['count']))
    return list_d


    
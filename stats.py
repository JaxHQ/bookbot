def get_num_words(text):
    words = text.split()
    return  len(words)
   

def char_dict(text):
    char_count = {}
    lowertext = text.lower()
    for char in lowertext:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
 

def sort_by(char_diction):
    return char_diction["count"] 

def sortedlist(dic_of_chars):
    charlist = []
    for char in dic_of_chars:
        count = dic_of_chars[char]
        # Create a dictionary with "char" and "count" keys
        char_diction = {"char": char, "count": count}
        charlist.append(char_diction)
    
    
    charlist.sort(reverse=True, key=sort_by)
    return charlist
       
        
    
    
    
             
        


import sys
from stats import get_num_words
from stats import char_dict
from stats import sortedlist

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    dic_of_chars = char_dict(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    sorted_chars = sortedlist(dic_of_chars)
        
    for char_diction in sorted_chars:
        char = char_diction["char"]
        if char.isalpha():
            count = char_diction["count"]
            print(f"{char}: {count}")
    
    print("============= END ===============")
     
        
 

    
main()

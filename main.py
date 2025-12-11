
import sys

def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import character_counter
from stats import sort_dict
from stats import format_for_dict

def main(): 
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    count_words(book_text)
    characters = character_counter(book_text)
    sorted_characters = sort_dict(characters)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")
    format_for_dict(sorted_characters)
    print("============= END ===============")
main()



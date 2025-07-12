import sys
from stats import *

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
     
    report()


    return 0

def report():
    file_name = sys.argv[1] 
    book = get_book_text(file_name)
    word_count = get_word_count(book)
    unique_character_dict = get_unique_character_count(book) 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    key, value = "char", "num"
    this_list = format_character_dictionary(unique_character_dict)
    for element in this_list:
        if element[key].isalpha():
            print(f"{element[key]}: {element[value]}")

    print("============= END ===============")

main()

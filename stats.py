import sys

def get_book_text(file_path):
    file_contents = None
    file_type = file_path.split(".")[-1] 
    if file_type != "txt":
        print(f"\".{file_type}\" is not a recognized file type. Use with \".txt\" files only.")
        sys.exit(1)
    try:
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"{file_path} is not found. Please check your file path and try again.")
        sys.exit(1)

def get_word_count(text):
    return len(text.split())

def get_unique_character_count(text):
    my_dict = {}
    my_string = text.lower()

    for character in my_string:
        if character in my_dict:
            my_dict[character] += 1
        else:
            my_dict[character] = 1 
    return my_dict

def sort_on(items):
    return items["num"]

def format_character_dictionary(d):
    new_list = []
    for key in d:
        new_list.append({"char": key, "num": d[key]})
    new_list.sort(reverse = True, key= sort_on)
    return new_list
    

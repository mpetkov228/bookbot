import sys
from stats import word_count

def main():
    if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
    book_path = sys.argv[1]

    with open(book_path) as f:
        file_contents = f.read()

    generate_report(book_path, file_contents)


def char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def generate_report(book_path, text):
    words = word_count(text)
    char_dict = char_count(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    for key in char_dict:
        if key.isalpha():
            print(f"'{key}: {char_dict[key]}'")
    print("--- End report ---")


main()
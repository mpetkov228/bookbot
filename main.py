def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    generate_report(file_contents)


def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def generate_report(text):
    words = word_count(text)
    char_dict = char_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for key in char_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {char_dict[key]} times")
    print("--- End report ---")


main()
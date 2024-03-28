def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_word_count = get_word_count(book_text)
    book_character_count = get_character_count(book_text)
    list_of_chars = []
    for key, value in book_character_count.items():
        list_of_chars.append({"character": key, "num": value})
    list_of_chars.sort(reverse=True, key=sort_on)
    get_report(book_path, book_word_count, list_of_chars)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in character_count.keys():
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def get_report(book_path, word_count, character_list):
    print(f"=== {book_path} ===")
    print(f"{word_count} words found in the document\n")
    for char in character_list:
        if char["character"].isalpha():
            print(f"The '{char['character']}' character was found {char['num']} times")


main()
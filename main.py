import sys

from stats import count_chars, how_many_words, sort_counted_chars


def get_book_text(file_path: str):
    with open(file_path) as file:
        return file.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    file_contents = get_book_text(file_path)
    words_count = how_many_words(file_contents)
    chars_dict = count_chars(file_contents)
    sorted_chars = sort_counted_chars(chars_dict)

    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()

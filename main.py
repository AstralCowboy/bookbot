from stats import number_of_words, count_chars, sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text


def main():
    text = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(text)} total words")
    print("--------- Character Count -------")

    chars = count_chars(text)
    sorted_chars = sorted_list(chars)
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
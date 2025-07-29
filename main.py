import sys

def get_book_text(books):
    with open(books) as f:
        book_contents = f.read()
    return book_contents

from stats import get_book_word_count

from stats import total_text

from stats import sort_text
    
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    total_word_count = get_book_word_count(get_book_text(sys.argv[1]))
    total_character_count = total_text(get_book_text(sys.argv[1]))
    sorted_count = sort_text(total_character_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print(f"--------- Character Count -------")
    for character in sorted_count:
        print(f"{character[0]}: {character[1]}")

if __name__ == "__main__":
    main()
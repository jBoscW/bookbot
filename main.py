from stats import get_num_words, count_characters, list_of_dicts
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2: 
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)

    num_words = get_num_words(book_text)
    list_d = list_of_dicts(count_characters(book_text))
    
    print(f'''============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------''')

    for i in list_d: 
        char = i['char']
        count = i['count']
        if char.isalpha():
            print(f'{char}: {count}')

    print('============= END ===============')


if __name__ == '__main__':
    main()


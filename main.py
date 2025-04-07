
# bookbot

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str): 
    return len(str.split())


def main():
    path = "books/frankenstein.txt"  # Adjust this path if your file is elsewhere
    text = get_book_text(path)
    num_words = count_words(text)
    print(f'{num_words} words found in the document')

if __name__ == '__main__':
    main()


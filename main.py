
# bookbot

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"  # Adjust this path if your file is elsewhere
    text = get_book_text(path)
    print(text)

main()

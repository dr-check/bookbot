import sys
from stats import count_words
from stats import count_characters
from stats import char_to_sort

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
path = sys.argv[1]
text = get_book_text(path)
word_count = count_words(text)
char_count = count_characters(text)
sorted_chars = char_to_sort(char_count)

def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():  
            print(f"{char}: {item['num']}")
    
    print("============= END ===============")

print_report(path, word_count, sorted_chars)








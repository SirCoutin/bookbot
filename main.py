import sys
from stats import wordCount, countLetters, organizeLetters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = (sys.argv[1])
    frankenstein = get_book_text(filepath)
    CountofWords =  wordCount(frankenstein)
    CountofLetters = countLetters(frankenstein)
    OrganizeLetters = organizeLetters(CountofLetters)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {filepath}')
    print("----------- Word Count ----------")
    print (f"Found {CountofWords} total words")
    print ("--------- Character Count -------")
    for org in OrganizeLetters:
        print(f'{org["char"]}: {org["num"]}')
    print ("============= END ===============")

main()
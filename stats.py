def wordCount(text):
    wordList = text.split()
    wordAmount = len(wordList)
    return wordAmount

def countLetters(text):
    text = text.lower()
    letters = {}
    for i in text:
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        else: 
            continue
    return letters

def organizeLetters(letters):
    char_list = []
    for char, num in letters.items():
        stats = {
            "char": char,
            "num": num
        }
        char_list.append(stats)
    char_list.sort(reverse = True, key=lambda item: item["num"])
    return char_list
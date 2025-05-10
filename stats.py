def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chardict = {}
    for i in text:
        i_lower = i.lower()
        if i_lower not in chardict:
            chardict[i_lower] = 1
        else:
            chardict[i_lower] += 1
    return chardict

def char_to_sort(chardict):
    char_list = [] 
    for char, count in chardict.items():
        char_data = {"char": char, "num": count}
        char_list.append(char_data)
    def sort_on(dict):
        return dict["num"]
    char_list.sort(key=sort_on, reverse=True)
    return char_list





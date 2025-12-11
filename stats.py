# File for functions to analyze text


#Counting how many words are in the text
def count_words(text):
    num_words = len(text.split())
    return num_words

#Counting how many characters are in the text
def character_counter(book_text):
    l_book = book_text.lower()
    char_dict = {}
    for word in l_book: 
        for c in word: 
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    return char_dict

#A sorting helper function
def sort_on(items):
        return items["num"]

#A function that creates a sorted list of dictionaries for characters and the number of times those characters show up            
def sort_dict(items):
    sorted_list = []

    for i in items:
        num = items[i] 
        combo = {"char" : i, "num" : num }
        sorted_list.append(combo)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

#A function to simplify the sorted dicitonary to look pretty 
def format_for_dict(sorted_list):
    for dict in sorted_list:
        if dict["char"].isalpha() == True: 
            print (f"{dict["char"]}: {dict["num"]}")
        else:
            None




 

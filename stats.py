def get_book_word_count(book_contents):
    words = book_contents.split()
    word_count = len(words)
    return word_count

def total_text(book_contents):
    lower_words = book_contents.lower()
    lower_words_list = list(lower_words)
    lower_words_dict = {
    }
    
    for character in lower_words_list:
        if character.isalpha():
        
            if character in lower_words_dict:
                lower_words_dict[character] += 1
            else:
                # dictionary[key] = 1
                lower_words_dict[character] = 1
    return lower_words_dict

def sort_on(items):
    return items[1]

def sort_text(lower_words_dict):
    data = list(lower_words_dict.items())
    data.sort(reverse=True, key=sort_on)
    return data
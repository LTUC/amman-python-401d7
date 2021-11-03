import re

some_text = "It was a {Adjective} and {Adjective} {Noun}."

parsed_text = "It was a {} and {} {}."
parsed_words = ["Adjective", "Adjective", "Noun"]

def parse(text):
    # new_list = []
    # parsed_text = re.sub(r'\{.*?\}', "{}", text)
    # parsed_words = re.findall(r'\{.*?\}', text)
    # for word in parsed_words:
    #     new_word = word.strip('{}')
    #     new_list.append(new_word)

    # return parsed_text, tuple(new_list)

    # Alternative simple way
    word = ""
    parsed_words = []
    parsed_text = ""
    status = 0 # outside of curly braces
    for ch in some_text:      
        if ch == "{":
            status = 1 # inside curly braces
            parsed_text = parsed_text + ch
        elif ch == "}":
            status = 0
            parsed_text = parsed_text + ch
            parsed_words.append(word)
            word = ""
        elif status == 0:
            parsed_text = parsed_text + ch
        else:
            word = word + ch
    return parsed_text, tuple(parsed_words)

if __name__ == "__main__":
    pt, pws = parse(some_text)
    print(pt, pws)
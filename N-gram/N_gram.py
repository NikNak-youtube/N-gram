from collections import Counter
import random

# get the text from the file
def get_text(file):
    with open(file, 'r') as f:
        text = f.read()
    return text

nochar = ".,!@#$%^&*()_+{}|:<>?`-=[]\';/1234567890"

# the text should be stored at the same directory as the code

word_counter = Counter()
word_list={}
def loop_text(text):
    words = text.split()
    for i in range(2, len(words)-1):
        key = (words[i-2].lower().strip(nochar), words[i-1].lower().strip(nochar), words[i].lower().strip(nochar))
        if key not in word_list:
            word_list[key] = [words[i+1]]
        else:
            word_list[key].append(words[i+1])
        word_counter[key] += 1
        
def quick_loop_text(file_name):
    text = get_text(file_name)
    loop_text(text)
quick_loop_text('text.txt')
quick_loop_text('Constitution.txt')
quick_loop_text('FrenchPolitics.txt')
quick_loop_text('Ship1.txt')
quick_loop_text('MobyDick.txt')
most_common = word_counter.most_common(100)
for item in most_common:
    # look for the key in the word_list
    print(item[0])
    print(word_list[item[0]])

# make a new generate_text function that allows for new versions of n in the n-gram
# the function should generate text of a specified length

def generate_text(word_list, length=1000):
    words = list(word_list.keys())
    current_key = random.choice(words)
    for i in range(length):
        print(current_key[2], end=' ')
        current_key = (current_key[0].lower(), current_key[1].lower(), current_key[2].lower().strip(nochar))
        next_words = word_list.get(current_key, None)
        if not next_words:
            break
        next_word = random.choice(next_words)
        current_key = (current_key[1].lower().strip(nochar), current_key[2].lower().strip(nochar), next_word)
generate_text(word_list)
    
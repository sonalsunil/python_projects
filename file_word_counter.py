import os
import string

def read_file():
    path=input("enter a file name:")
    if os.path.isfile(path):
        with open (path,"r") as f:
            data=f.read()
            return data
    else:
        print("file does not exist")

def count_words(data):
    words=data.split()
    count=0
    for w in words:
        w=w.strip()
        w=w.lower()
        w=w.translate(str.maketrans("", "", string.punctuation))
        if w and any(ch.isalpha() for ch in w):
            count+=1
    return count

def count_lines(data):
    if not data.strip():
        return 0

    lines = data.splitlines()
    return len(lines)

def count_alphabets(data):
    i=0
    for w in data:
        if(w.isalpha()):
            i=i+1
    return i

def count_characters(data):
   return len(data)

def word_frequency(data):
    words = data.split()
    freq={}
    for w in words:
        w=w.strip()
        w=w.lower()
        w=w.translate(str.maketrans("", "", string.punctuation))
        if w and any(ch.isalpha() for ch in w):
            if w in freq:
                freq[w]+=1
            else:
                freq[w]=1
    return freq

def most_common_word(freq):
    if not freq:
        print("No words found in the file")
        return []
   
    maxfreq=max(freq.values())
    word_list=[]
    for word, count in freq.items():
        if(count==maxfreq):
            word_list.append(word)
    return word_list


# MAIN PROGRAM
data = read_file()

if data is not None:

    # 1. Count words
    word_count = count_words(data)
    print("Total words:", word_count)

    # 2. Count lines
    line_count = count_lines(data)
    print("Total lines:", line_count)

    # 3. Count characters
    char_count = count_characters(data)
    print("Total characters:", char_count)

    # 4. Count alphabets
    alphabet_count = count_alphabets(data)
    print("Total alphabets:", alphabet_count)

    # 5. Calculate word frequency
    freq_count = word_frequency(data)
    print("Word frequency:", freq_count)

    # 6. Find most common word
    common_word = most_common_word(freq_count)
    print("Most common word(s):", common_word)
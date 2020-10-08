#!/usr/local/bin/python3
from string import punctuation

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def format_word_freq(wf):
    """
     Return a string of the word frequency dictionary wf formatted for printing.
    """
    format_width = max(len(w) for w in wf)
    output_string = ""

    for w in sorted(wf, key=wf.get, reverse=True):
        count = wf[w]
        output_string += f"{w:>{format_width}} : {count} {'*' * count}\n"
    
    return output_string

def is_punct(s):
    """ 
    Return true if s contains only punctuation characters.
    """
    return s.isprintable() and not (s.isalpha() or s.isspace() or s.isdigit())


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    
    # 1: read the contents of file
    with open(file):
        words = wordsfile.read()
    
    #print(words)

    # 2: convert the text to lowercase
    words = words.lower()

    #print(words)

    # 3: remove punctuation 
    #  iterate through all punctuation characters
    for p in punctuation:
    
    # remove punctuation character from words and reassign words
    words = words.replace(p, '')

    #print(words)

    # 4: break file contents to words
    wordlist = words.split()

    #print(wordslist)

    # 5: remove STOP_WORDS
    for s_w in STOP_WORDS:
        while s_w in wordlist:
            wordlist.remove(s_w)

    #print(wordslist)

    # 6: words counts, create a dictionary to hold words counts, 
    # iterate through the words in wordslist, check if word exist +1
    #if doesn't set to 1

    
    wordscounts = {}
    for w in wordslist:
        if w in wordscounts:
            wordscounts[w] += 1

        else:
            wordscounts[w] = 1 

            #print(wordscounts) 

    # 7 get formatted output and print
    formatted = format_world_freq(wordscounts)
    print(formatted)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

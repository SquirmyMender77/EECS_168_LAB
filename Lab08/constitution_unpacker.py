def build_count(us_constitution):
    clean_words=[]
    with open('us_constitution.txt', 'r') as const:
        for line in const:
            line = line.strip()
            line =line.lower()
            new_line=""
            for ch in line:
                if "a"<= ch <="z" or "A" <= ch <= "Z":
                    new_line+= ch
                else:
                    new_line += " "
            words= new_line.split()
            for w in words:
                clean_words.append(w)
    counts={}
    for word in clean_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
def clean_word(us_constitution):
    clean_words=[]
    with open('us_constitution.txt', 'r') as const:
        for line in const:
            line = line.strip().lower()
            new_line=""
            for ch in line:
                if "a"<= ch <="z":
                    new_line+= ch
                else:
                    new_line += " "
            words= new_line.split()
            clean_words.extend(words)
        return clean_words

def unique_words(word_counts):
    counts = build_count('us_constitution.txt')
    unique_count = sum(1 for word in counts if counts[word] ==1)
    return unique_count
    
def main():
    welcome ="Welcome to the word counter!"
    print(welcome.center(40,"="))
    words = clean_word("us_constitution.txt")
    counts = build_count("us_constitution.txt")
    unique_count = unique_words("us_constitution.txt")
    with open("word_count.txt", "w") as wo:
        for word, count in counts.items():
            wo.write(f"{word}: {count}\n")
            
    with open("unique_words.txt", 'w') as uni:
        uni.write(f"Number of words that appear only once: {unique_count}\n")
    print(f"Total words: {len(words)}")
    print(f"Unique words (appear once): {unique_count}")
           
main()

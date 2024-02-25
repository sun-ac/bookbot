def main():
    generate_report("books/frankenstein.txt")

def generate_report(file):
    print(f"--- Begin report of {file} ---")
    text = text_from_file(file)
    letter_counts = count_letters(text)
    print(f"{count_words(text)} words found in the document")
    letter_counts = sorted(letter_counts.items(), key = lambda item: item[1], reverse=True)
    for letter_count in letter_counts:
        if letter_count[0].isalpha():
            print(f"The {letter_count[0]} character was found {letter_count[1]} times")
    print("--- End report ---")

def text_from_file(file):
    with open(file) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    letter_counts = {}
    for letter in text:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

main()

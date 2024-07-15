import nltk
from nltk.corpus import wordnet as wn
import os
import socket
import time

# Define the custom data path
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

# Add the custom data path to nltk's data path
nltk.data.path.append(nltk_data_path)

# Download the required resources to the custom path if not already present
nltk.download('wordnet', download_dir=nltk_data_path)
nltk.download('omw-1.4', download_dir=nltk_data_path)

# Set a default timeout for socket operations
socket.setdefaulttimeout(10)  # 10 seconds timeout

class QuitProgramException(Exception):
    pass

def get_input(prompt, quit_keyword='q'):
    user_input = input(prompt).strip()
    if user_input.lower() == quit_keyword.lower():
        raise QuitProgramException
    return user_input

def fetch_meaning_nltk(word):
    synsets = wn.synsets(word)
    meanings = {}
    for synset in synsets:
        pos = synset.pos()
        definition = synset.definition()
        if pos in meanings:
            meanings[pos].append(definition)
        else:
            meanings[pos] = [definition]
    return meanings

def fetch_synonyms_nltk(word):
    synonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def fetch_antonyms_nltk(word):
    antonyms = set()
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma.antonyms():
                antonyms.add(lemma.antonyms()[0].name())
    return list(antonyms)

def fetch_examples_nltk(word):
    examples = []
    for synset in wn.synsets(word):
        examples.extend(synset.examples())
    return examples

def quit_program():
    print("Quitting the program. Goodbye!")
    exit()

def main():
    print("\nWelcome to the Word Dictionary!")
    print("This tool provides definitions, synonyms, antonyms, and examples for English words.")
    print("You can press 'q' at any prompt to quit the program.")

    while True:
        try:
            word = get_input("Enter a word to lookup (or 'q' to quit): ").strip().lower()
            print(f"\nWord: {word.capitalize()}")

            # Definitions
            meanings = fetch_meaning_nltk(word)
            if meanings:
                print("Definitions:")
                for pos, definitions in meanings.items():
                    print(f"{pos.capitalize()}:")
                    for definition in definitions:
                        print(f"  - {definition}")
            else:
                print("No definitions found.")

            # Synonyms
            synonyms = fetch_synonyms_nltk(word)
            if synonyms:
                print("\nSynonyms:")
                print(", ".join(synonyms))
            else:
                print(f"{word} has no Synonyms in the API")

            # Antonyms
            antonyms = fetch_antonyms_nltk(word)
            if antonyms:
                print("\nAntonyms:")
                print(", ".join(antonyms))
            else:
                print(f"{word} has no Antonyms in the API")

            # Examples
            examples = fetch_examples_nltk(word)
            if examples:
                print("\nExamples:")
                for example in examples:
                    print(f"  - {example}")
            else:
                print(f"{word} has no Examples in the API")

            print()  # Add a blank line for readability between words

        except QuitProgramException:
            quit_program()

if __name__ == "__main__":
    main()

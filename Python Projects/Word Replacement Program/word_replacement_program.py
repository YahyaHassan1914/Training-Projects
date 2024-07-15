def replace_word(text, word_to_replace, word_replacement):
    return text.replace(word_to_replace, word_replacement)

def read_from_user_input():
    text = input("Enter the text: ")
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    return text, word_to_replace, word_replacement

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    return text, word_to_replace, word_replacement

def main():
    choice = input("Do you want to read input from (1) user or (2) file? Enter 1 or 2: ")
    
    if choice == '1':
        text, word_to_replace, word_replacement = read_from_user_input()
    elif choice == '2':
        file_path = input("Enter the path to the .txt file: ")
        text, word_to_replace, word_replacement = read_from_file(file_path)
    else:
        print("Invalid choice. Exiting.")
        return
    
    new_text = replace_word(text, word_to_replace, word_replacement)
    print("\nOriginal Text:\n", text)
    print("\nModified Text:\n", new_text)

if __name__ == "__main__":
    main()
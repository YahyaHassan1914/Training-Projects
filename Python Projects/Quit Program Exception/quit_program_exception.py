class QuitProgramException(Exception):
    pass

def get_input(prompt, quit_keyword='Q'):
    user_input = input(prompt).strip()
    if user_input.upper() == quit_keyword.upper():
        raise QuitProgramException
    return user_input

def quit_program():
    print("Quitting the program. Goodbye!")
    exit()

# How to use?
# Still under production

"""
    quit_keyword = input("Enter the keyword to quit the program (default is 'q'): ").strip().upper() or 'Q'
    print(f"You can press '{quit_keyword}' at any prompt to quit the program.")

    input = get_input("Input", quit_keyword)

    try:
    
    except QuitProgramException:
        quit_program()
"""
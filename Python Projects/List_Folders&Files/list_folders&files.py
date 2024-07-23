import os
from collections import defaultdict

def search_dir(dir_path, indent_level=0):
    current_path_list = os.listdir(dir_path)
    for c in current_path_list:
        full_path = os.path.join(dir_path, c)
        if not os.path.isdir(full_path):
            print("    " * (indent_level + 1) + c)
        else:
            print("    " * (indent_level + 1) + "\\" + c)
            search_dir(full_path, indent_level + 1)

def main():
    dir_path = 'D:\\Test'
    print(dir_path)
    search_dir(dir_path)

if __name__ == "__main__":
    main()
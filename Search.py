import os
import sys

print("Type 'exit' to exit the program.")
print("Type 'help' for help.")
print("Type '=' for 'equal' mode.")
print("Type 'sw' for 'starts with' mode.")
print("Type 'ew' for 'ends with' mode.")
print("Enter the name of the file you want to search.")
print("For example: 'Viber.exe', 'text.txt', or 'image.jpg'.\n")

hlp = "This is the help menu. Use the specified commands to search for files on your computer."
while True:
    cmd = input("What file are you looking for? \n")
    if cmd == 'exit':
        sys.exit()
    elif cmd == 'help':
        print(hlp)
    elif cmd == '=':
        print("Search mode: Exact match. Enter the file name you want to find.")
        cmd = input("Enter the file name: \n")
        print("Searching for the exact file. Please wait...")
        for root, dirs, files in os.walk('/'):
            for file in files:
                if file == cmd:
                    filename = os.path.join(root, file)
                    print('File found at: ' + filename)
                    while True:
                        of = input("Do you want to open this file? (y/n): \n")
                        if of == 'exit':
                            sys.exit()
                        elif of == 'help':
                            print(hlp)
                        elif of == "y":
                            os.startfile(filename)
                            print("Searching for more matching files...\n")
                            break
                        elif of == "n":
                            print("Searching for more matching files...\n")
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.\n")
    elif cmd == 'sw':
        print("Search mode: Files starting with your input.")
        cmd = input("Enter the starting string: \n")
        print("Searching for files that start with your input. Please wait...")
        for root, dirs, files in os.walk('/'):
            for file in files:
                if file.startswith(cmd):
                    filename = os.path.join(root, file)
                    print('File found at: ' + filename)
                    while True:
                        of = input("Do you want to open this file? (y/n): \n")
                        if of == 'exit':
                            sys.exit()
                        elif of == 'help':
                            print(hlp)
                        elif of == "y":
                            os.startfile(filename)
                            print("Searching for more matching files...\n")
                            break
                        elif of == "n":
                            print("Searching for more matching files...\n")
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.\n")
    elif cmd == 'ew':
        print("Search mode: Files ending with your input.")
        cmd = input("Enter the ending string: \n")
        print("Searching for files that end with your input. Please wait...")
        for root, dirs, files in os.walk('/'):
            for file in files:
                if file.endswith(cmd):
                    filename = os.path.join(root, file)
                    print('File found at: ' + filename)
                    while True:
                        of = input("Do you want to open this file? (y/n): \n")
                        if of == 'exit':
                            sys.exit()
                        elif of == 'help':
                            print(hlp)
                        elif of == "y":
                            os.startfile(filename)
                            print("Searching for more matching files...\n")
                            break
                        elif of == "n":
                            print("Searching for more matching files...\n")
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.\n")
    else:
        print("Searching for files containing your input. Please wait...")
        for root, dirs, files in os.walk('/'):
            for file in files:
                if cmd in file:
                    filename = os.path.join(root, file)
                    print('File found at: ' + filename)
                    while True:
                        of = input("Do you want to open this file? (y/n): \n")
                        if of == 'exit':
                            sys.exit()
                        elif of == 'help':
                            print(hlp)
                        elif of == "y":
                            os.startfile(filename)
                            print("Searching for more matching files...\n")
                            break
                        elif of == "n":
                            print("Searching for more matching files...\n")
                            break
                        else:
                            print("Please enter 'y' for yes or 'n' for no.\n")

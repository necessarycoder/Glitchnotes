import os
print("welcome to GlitchNotes!\ntype help for list of commands")
using = 1
while using == 1:
    command = input()
    command.lower()
    if command == "help":
        print("list of commands:\nnotes (view all notes)\nnote (view note content)\nrewrite (rewrite note content)\nappend (append note content)\ncreate (create new note)\ndelete (delete note)")
    elif command == "notes":
        os.listdir(notes)
    elif command == "create":
        name = input("enter note\'s name: ")
        try:
            file = open("notes/"+name, "r")
            file.close()
            print("error: file already exists")
            break
        except FileNotFoundError:
            file = open("notes/"+name, "w")
            file.close()
    elif command == "delete":
        name = input("enter note\'s name: ")
        os.system("rm notes/"+name)
    elif command == "rewrite":
        name = input("enter note's name: ")
        content = input("enter note's new content: ")
        file = open("notes/"+name, "w")
        file.write(content)
        file.close()
    elif command == "append":
        name = input("enter note's name: ")
        content = input("enter additional content for note: ")
        file = open("notes/"+name, "a")
        file.append(content)
        file.close()
    elif command == "note":
        name = input("enter note's name: ")
        file = open("notes/"+name, "r")
        content = file.read()
        file.close()
        print(content)

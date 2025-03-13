
try:
    file=open("demo.txt","r")
    new=file.read()
    if not new:
        print("The file is empty")
    else:
        print(new)
except FileNotFoundError:
    print("file  not found")
except UnicodeDecodeError:
    print("The file contains invalid data")


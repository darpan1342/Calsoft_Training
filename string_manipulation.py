import random

string = input("Enter the text:")
if len(string) :
    print(string.upper())
    count = 0
    for i in string.split():
         count = count + 1
    print(count)
             
else:
    print("Empty string therefore opening file.txt file ")
    try:
        f = open('file.txt','r')
        text = f.read()
        txt = text.split('\n')
        n = int(random.randrange(0,len(txt)))
        t = txt[n]
        print(t.upper())
        count = 0
        for i in t.split():
            count = count + 1
        print(count)
             

    except FileNotFoundError:
        print("File dosen't exist")
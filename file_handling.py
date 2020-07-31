try:
    f = open('file.txt','r+')
    text = f.read()
    txt = text.split('\n')[-1]
    t = int(txt.split(' ')[1])
    string = "\nIteration " + str(t+1) + " file-handling"
    f.write(string)

except FileNotFoundError:
    f = open('file.txt','w')
    f.write("Iteration 1 file-handling")
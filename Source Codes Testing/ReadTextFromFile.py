fhand = open(input("Enter the file which you want to parse:\t"), 'r')
for lines in fhand:
    line = lines.rstrip()
    words = line.strip()
    print(words)

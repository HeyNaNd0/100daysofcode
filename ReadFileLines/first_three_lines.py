'''
creating this to learn how to read input from a random file
'''

with open('randomLines.txt', encoding="utf-8") as file:
    content = file.read()
    lines=content.split('.')
    first3Lines=lines[0:3]
    print("First 3 lines of the file:")
    for line in first3Lines:
        print(f"{line.strip()}.")
# End-of-file (EOF)

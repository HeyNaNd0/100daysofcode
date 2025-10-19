'''
creating this to learn how to read input from a random file
'''

with open('randomLines.txt', 'r') as file:
    content = file.read()
    print(type(content))
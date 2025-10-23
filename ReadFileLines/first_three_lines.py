'''
creating this to learn how to read input from a random file
'''

try:
    with open('randomLines.txt', encoding="utf-8") as file:
        lines = file.readlines()
        first_3_lines = lines[0:3]
        print("First 3 lines of the file:")
        for line in first_3_lines:
            print(line.rstrip('\n'))
except FileNotFoundError:
    print("Error: 'randomLines.txt' not found.")
except IOError as e:
    print(f"Error reading file: {e}")
# End-of-file (EOF)

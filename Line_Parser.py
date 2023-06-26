# Function to parse a line and extract the file name, paragraph number, line number, and value
def parse_line(string):
    # Split the line using forward slashes (/)
    digits = string.rsplit('/', 3)
    
    # Check if the line contains the required number of slashes
    if string.count('/') < 3:
        return None
    else:
        # Validate that the second, third, and fourth parts contain only digits
        for i in digits[1]:
            if i.isalpha():
                return None
        for a in digits[2]:
            if a.isalpha():
                return None
        for c in digits[3]:
            if c.isalpha():
                return None
        
        # Return the extracted values as a tuple (fname, parno, lineno, value)
        Tuple = (digits[1], digits[2], digits[3], digits[0])
        return Tuple

# Function to get a specific line from a list of lines
def get_line(lines, parno, lineno):
    # Get the specified line
    starting_line = lines[parno - 1][lineno - 1]
    return starting_line

# Main script execution

# Get input from the user for the file number, paragraph number, and line number
fname = input("Please enter the file number ==> ")
parno = int(input("Please enter the paragraph number ==> "))
lineno = int(input("Please enter the line number ==> "))

lines = []

# Read the file and store the lines in memory
with open(fname + '.txt', encoding='utf8') as file:
    paragraph = []
    for line in file:
        line = line.strip()
        if line:
            paragraph.append(line)
        else:
            lines.append(paragraph)
            paragraph = []
    if paragraph:
        lines.append(paragraph)

f_out = open('program.py', 'w')

while True:
    # Check if the termination condition is met
    if fname == '0' and parno == 0 and lineno == 0:
        break

    # Parse the line and retrieve the list of values
    List = parse_line(get_line(lines, parno, lineno))
    
    # Check if the line was successfully parsed
    if List is not None:
        # Write the value to the output file
        f_out.write(List[3])
        f_out.write('\n')
        
        # Update the variables with the new values
        fname = List[0]
        parno = int(List[1])
        lineno = int(List[2])

# Close the output file
f_out.close()

# Read and print the contents of the 'program.py' file
with open('program.py', 'r', encoding='utf-8') as file2:
    for line in file2:
        print(line)

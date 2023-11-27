# input() will read in string
num=input()
print(num)

# if user does not enter a number an exception will be thrown. 
# use try/except
try:
    num=int(input("Enter a number: "))
    print(num)
    sum=num+2
except:
    print("you did not enter a number")

# open file and store each line in a list called file
with open("movies.txt") as file:
    for line in file:
        # strip off the end line
        print(line.strip())

# create empty dictionary
heights = {}
with open("heights.txt") as file:
    for line in file:
        # strip off end of line
        stripped_line=line.strip()
        # split each word separated by a space and store in the list tokens
        tokens = stripped_line.split()
        print(tokens)
        heights[tokens[0]+ ' ' + tokens[1]] = tokens[2]
print(heights)
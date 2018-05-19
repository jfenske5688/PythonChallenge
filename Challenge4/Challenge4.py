import re

def main():
    inputFile = "Challenge4.txt"
    inputString = ""

    with open(inputFile, 'rb') as f:
        inputString = "".join(f.read().split())

    searchPattern = '[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'
    searchPatternLowercase = '[a-z]'
    searchPatternUppercase = '[A-Z]'

    matches = re.findall(searchPattern, inputString)

    print("".join(matches))



if __name__ == "__main__":
    main()
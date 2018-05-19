from collections import defaultdict

def main():
    stringFile = "Challenge3.txt"
    inputString = ""

    with open(stringFile, 'rb') as f:
        inputString = f.read()

    charCountDct = defaultdict(int)

    for char in inputString:
        charCountDct[char] += 1

    rarestCount = len(inputString)

    for key, val in charCountDct.iteritems():
        if val < rarestCount: rarestCount = val

    rareChars = []
    for key, val in charCountDct.iteritems():
        if val == rarestCount: rareChars.append(key)

    print "".join(rareChars)

if __name__ == "__main__":
    main()
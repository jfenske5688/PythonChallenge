import re
import sys
import urllib2
from bs4 import BeautifulSoup
from bs4 import Comment


def main():
    response = urllib2.urlopen(challengeURL)
    pageSource = response.read()

    soup = BeautifulSoup(pageSource, 'html.parser')
    data = soup.find_all(string=lambda text: isinstance(text, Comment))

    try:
        # do this to get rid of whitespace characters in comment
        inputString = "".join(data[-1].split())
    except IndexError, ie:
        print("Could not get comment from URL")
        sys.exit(1)
    else:
        outerSearchPattern = '[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+'

        matches = re.findall(outerSearchPattern, inputString)

        print("".join(matches))


if __name__ == "__main__":
    challengeURL = 'http://www.pythonchallenge.com/pc/def/equality.html'
    main()
import sys
import urllib2
from bs4 import BeautifulSoup

def main():
    response = urllib2.urlopen(challengeURL)
    pageSource = response.read()

    soup = BeautifulSoup(pageSource, 'html.parser')

    print(soup.find_all('a', href=True))

if __name__ == "__main__":
    challengeURL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
    main()
import urllib2

def main():
    response = urllib2.urlopen(challengeURL)
    pageSource = response.read()

    print(pageSource)

if __name__ == "__main__":
    challengeURL = "http://www.pythonchallenge.com/pc/def/ocr.html"
    main()
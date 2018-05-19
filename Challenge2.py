from string import maketrans

def main():
    transIn = 'abcdefghijklmnopqrstuvwxyz'
    transOut = transIn[2:] + transIn[0:2]
    transMap = maketrans(transIn, transOut)

    inputString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print(inputString.translate(transMap))

    url = 'map'

    print(url.translate(transMap))

if __name__ == "__main__":
    main()
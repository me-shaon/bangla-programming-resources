#This script helps to create the lexicographic order in the author list file
#How to: Just add a blog link in the existing 'blog-list.md' file and run this script

import re
import collections

fileName = "blog-list.md"

headerStub = """
## যাদের ব্লগ থেকে লেখা সংগ্রহ করা হয়েছেঃ

#### ব্লগের তালিকা (লেখকের নামের ক্রমানুসারে):

"""

def main():
    authorNames = getAuthorList()
    sortedNames = collections.OrderedDict(sorted(authorNames.items()))
    writeToFile(sortedNames)


def getAuthorList():
    nameDict = {}
    with open(fileName, "r", encoding="utf8") as file:
        for line in file:
            nameMatched = re.match(r'^- \[(.*)\]\((.*)\)', line, re.UNICODE) #Find only the blog links
            if nameMatched:
                nameDict[nameMatched.group(1)] = nameMatched.group(2)
    return nameDict


def writeToFile(sortedNames):
    with open(fileName, "w", encoding="utf8") as file:
        file.write(headerStub)

        for k, v in sortedNames.items():
            line = "- [{0}]({1})".format(k, v)
            file.write(line + '\n')


if __name__ == '__main__':
    main()

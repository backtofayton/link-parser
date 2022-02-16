# add the urls that you want to parse into 'pagesToCrawl.txt' file and run the script
# you can see the results in 'links.txt' file and html response at 'response.txt'

import requests
import re

fileName = 'response.txt'
linksFileName = 'links.txt'

crawlingList = []
with open('./pagesToCrawl.txt', 'r', encoding='utf8') as source:
    for line in source:
        crawlingList.append(line.strip())

print(crawlingList)

resetFile = open(fileName, 'w')
resetFile.close()
for eachAddress in crawlingList:
    print(eachAddress)
    if not re.match('https?://', eachAddress):
        eachAddress = 'http://' + eachAddress
    print(eachAddress)
    requ = requests.get(eachAddress, stream=True)
    with open(fileName, 'ab') as fd:
        for chunk in requ.iter_content(chunk_size=128):
            fd.write(chunk)

# print(requ.raw)
# print(requ.raw.read(10))
# print(requ)
print(requ.encoding)

# reSearch = re.search('https?.* ', 'http://docs.python.org/3/library/re.html style""')
# print(reSearch.group())

# searchString = 'http://docs.python.org/3/library/re.html style""'
#
# reFindall = re.findall('https?.* ', searchString)
# print(reFindall)
#
reCompile = re.compile('https?://.*?[" ]')
# print(reCompile.findall(searchString))

linkList = []
with open(fileName, 'r', encoding='utf8') as fd:
    count = 0
    for line in fd:
        count = count + 1
        try:
            # print(str(count) + ': ' + line)
            linkList.extend(reCompile.findall(line))
        except:
            linkList.append('error')
    # print(str(count) + ': ' + 'error')

# print(linkList)

with open(linksFileName, 'w') as linksFile:
    for eachLink in linkList:
        linksFile.write(eachLink.strip('"') + '\n')

print(f'Successfully created {linksFileName} with links from {crawlingList}')

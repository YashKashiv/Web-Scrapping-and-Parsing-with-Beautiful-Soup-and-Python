import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
soup = bs.BeautifulSoup(source, "lxml") # it will make scrapped website code (source) understandable

#print(soup)
#print(soup.title)
#print(soup.title.name) # will print tage name
#print(soup.title.string)
#print(soup.p) # will print 1st paragraph element
#print(soup.find_all("p")) # will print all the paragraph text
#print(soup.get_text(""))

'''for paragraph in soup.find_all("p"):
    #print(paragraph.string) # some of strings which have child tag it will return as none for that we will use .text
    print(paragraph.text)'''

for url in soup.find_all("a"): # scrap through tag name basically links in anchor tag
    print(url.get("href"))
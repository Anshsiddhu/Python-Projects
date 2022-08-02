from bs4 import BeautifulSoup
import requests

url = "https://codewithharry.com/"
content = requests.get(url)
htmlcontent = content.content
# print(htmlcontent)
soup = BeautifulSoup(htmlcontent , 'html.parser')
# print(soup.prettify)
# Get the html title
# title = soup.title
# commonly used objects of bs4:
# print(type(title))#1. Tag
# print(type(title.string))#2. Navigable string
# print(type(soup))#3. BeautifulSoup
# 4. Comment
# Get all the paragraphs of the page
# paras = soup.find_all('p')
# print(paras)

# print(anchors)
# get the html content in  body tag
# body = soup.find_all('body')
# print(body)
# get the first para tag content(first element of html page)
# print(soup.find('p'))
# get the class of any content
# print(soup.find('p')['class'])
# find all the elements with any class
# print(soup.find_all("p", class_="lead"))
# get the text from the elements
# print(soup.find('p').get_text())
# get all the text from the html page
# print(soup.get_text())
# Get all the anchor tags of the page
# anchors = soup.find_all('a')
# all_links = set()
# get all the links on the page

# for link in anchors:
# if(link.get('href') != '#'):
# linkText= ("https://codewithharry.com" +link.get('href'))
# all_links.add(link)
# print(linkText)
#.children = A tag's children are available as a generator
#.contents = A tag's children are available as a list
navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
#for children
#for elem in navbarSupportedContent.children:
 #   print(elem)
#for item in navbarSupportedContent.strings:
 #print(item)
#for item in navbarSupportedContent.stripped_strings:
 #print(item)
 #prints parent
#for item in navbarSupportedContent.parents:
    #print(item.name)
#for siblings
#print(navbarSupportedContent.next_sibling)
#print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)
elem = soup.select('.modal-footer')
print(elem)

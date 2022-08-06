from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.string)
#print(soup.prettify())

#print(soup.a)
#print(soup.li)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)

# for tag in all_anchor_tags:
#     #print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
#print(heading)

section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.get("class"))

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)

list_a = soup.select("li a")
print(list_a)
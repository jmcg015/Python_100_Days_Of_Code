from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("a", class_="titlelink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvote)

# Get largest number from upvote list
max_num = max(article_upvote)
max_num_index = article_upvote.index(max_num)
# Get index position of largest number
# Use that index position to get the text for article
print(article_texts[max_num_index])
print(article_links[max_num_index])
# Use index position to get article link
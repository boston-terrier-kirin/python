import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")

links = soup.select(".titleline")
subtexts = soup.select(".subtext")


def sort_news_by_votes(news):
    return sorted(news, reverse=True, key=lambda d: d["votes"])


def create_custom_news(links, subtexts):
    news = []

    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        vote = subtexts[index].select(".score")

        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if (points > 200):
                news.append({
                    "title": title,
                    "link": href,
                    "votes": points
                })

    return sort_news_by_votes(news)


pprint.pprint(create_custom_news(links, subtexts))

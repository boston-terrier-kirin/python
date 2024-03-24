from bs4 import BeautifulSoup

SIMPLE_HTML = """
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is a title</h1>
    <p class="subtitle">subtitle, Lorem ipsum dolor sit amet.</p>
    <p>Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet.</p>
    <ul>
        <li>Rolf</li>
        <li>Charlie</li>
        <li>Jen</li>
        <li>Jose</li>
    </ul>
</body>
</html>
"""

simple_soup = BeautifulSoup(SIMPLE_HTML, "html.parser")


def find_title():
    h1_tag = simple_soup.find("h1")
    print(h1_tag.string)


def find_list_item():
    list_items = simple_soup.find_all("li")
    list_contents = [e.string for e in list_items]
    print(list_contents)


def find_subtitle():
    p = simple_soup.find("p", {"class": "subtitle"})
    print(p.string)


def find_other_paragraph():
    p = simple_soup.find_all("p")
    other_paragraph = [e for e in p if "subtitle" not in e.attrs.get("class", [])]
    print(other_paragraph)


find_other_paragraph()

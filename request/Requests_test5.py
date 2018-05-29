from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">The Dormouse's story</p>
<!--def -->
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
print(type(html_doc))
soup = BeautifulSoup(html_doc,"html.parser")
#print(soup.a)
print(soup.text)
print(soup.attrs)
#print(type(soup.p.string))

